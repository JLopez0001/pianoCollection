from django.urls import path, include
from .views import Home, PianoList,PianoDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pianos/', PianoList.as_view(), name='Piano-list'),
    path('pianos/<int:id>/', PianoDetail.as_view(), name='Piano-detail'),

]
