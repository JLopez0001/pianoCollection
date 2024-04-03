from django.urls import path, include
from .views import Home, PianoList,PianoDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pianos/', PianoList.as_view(), name='Piano-list'),
    path('pianos/<int:id>/', PianoDetail.as_view(), name='Piano-detail'),
    path('pianos/<int:id>/maintenance/', MaintenanceListCreate.as.view(), name='maintenance-list-create'),
    path('pianos/<int:id>/maintenance/<int:id>', MaintenanceDetail.as.view(), name='maintenance-detail')
]
