from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Piano, MaintenanceRecord, Performer
from .serializers import PianoSerializer, MaintenanceRecordSerializer, PerformerSerializer

# Create your views here.

# Define the home view
class Home(APIView):
  def get(self, request):
      content = {'message': 'Welcome to the cat-collector api home route!'}
      return Response(content)

#This will get all the pianos in the database
class PianoList(generics.ListCreateAPIView):
  queryset = Piano.objects.all()
  serializer_class = PianoSerializer

#Gets a specific piano
class PianoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Piano.objects.all()
  serializer_class = PianoSerializer
  lookup_field = 'id'


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