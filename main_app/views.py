from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied # include this additional import
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Piano, MaintenanceRecord, Performer
from .serializers import PianoSerializer, MaintenanceRecordSerializer, PerformerSerializer, UserSerializer

# Create your views here.

# Define the home view
class Home(APIView):
  def get(self, request):
      content = {'message': 'Welcome to the cat-collector api home route!'}
      return Response(content)

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self,request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
      return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username = request.user)
    refresh = RefreshToken.for_user(request.user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })


#This will get all the pianos in the database
class PianoList(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = PianoSerializer

  def get_queryset(self):
    # This ensures we only return pianos belonging to the logged-in user
    user = self.request.user
    return Piano.objects.filter(user = user)

  def perform_create(self, serializer):
    # This associates the newly created cat with the logged-in user
    serializer.save(user = self.request.user)


#Gets a specific piano
class PianoDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PianoSerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return Piano.objects.filter(user=user)

  def perform_update(self, serializer):
    piano = self.get_object()
    if piano.user != self.request.user:
      raise PermissionDenied({"message": "You do not have permission to edit this cat."})
    serializer.save()

  def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this cat."})
    instance.delete()


#Retrieves all Maintenace list for that specific piano
class MaintenanceListCreate(generics.ListCreateAPIView):
    serializer_class = MaintenanceRecordSerializer
    def get_queryset(self):
      piano_id = self.kwargs['piano_id']
      return MaintenanceRecord.objects.filter(piano_id=piano_id)

    def perform_create(self,serializer):
      piano_id = self.kwargs['piano_id']
      piano = Piano.objects.get(id=piano_id)
      serializer.save(piano=piano)


class MaintenanceDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = MaintenanceRecordSerializer
  lookup_field = 'id'

  def get_queryset(self):
    piano_id = self.kwargs['piano_id']
    return MaintenanceRecord.objects.filter(piano_id = piano_id)
 

class PerformerCreate(generics.ListCreateAPIView):
  queryset = Performer.objects.all()
  serializer_class = PerformerSerializer


class PerformerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Performer.objects.all()
  serializer_class = PerformerSerializer
  lookup_field = 'id'

  def retrieve(self, request, *args, **kwars):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    pianos_not_associated = Piano.objects.exclude(id=instance.id)
    pianos_serializer = PianoSerializer(pianos_not_associated, many=True)

    return Response({
        'piano': serializer.data,
        'pianos_not_associated': pianos_serializer.data
    })

class AddPerformerToPiano(APIView):
  def post(self, request, piano_id, performer_id):
      piano = Piano.objects.get(id=piano_id)
      performer = Performer.objects.get(id=performer_id)
      piano.performer.add(performer)
      return Response({'message': f'Performer {performer.name} added to Piano {piano.brand}'})


class RemovePerformerFromPiano(APIView):
  def post(self, request, piano_id, performer_id):
    piano = Piano.objects.get(id=piano_id)
    performer = Performer.objects.get(id=performer_id)
    piano.performer.remove(performer)
    return Response({'message': f'Performer {performer.name} Removed to Piano {piano.brand}'})
