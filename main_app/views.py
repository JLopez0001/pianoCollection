from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# Define the home view

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the cat-collector api home route!'}
        return Response(content)