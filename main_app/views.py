from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Piano
from .serializers import PianoSerializer

# Create your views here.

# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the cat-collector api home route!'}
        return Response(content)

class PianoList(generics.ListCreateAPIView):
  queryset = Piano.objects.all()
  serializer_class = PianoSerializer

class PianoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Piano.objects.all()
  serializer_class = PianoSerializer
  lookup_field = 'id'
