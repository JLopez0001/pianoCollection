from django.urls import path, include
from .views import Home, PianoList,PianoDetail, MaintenanceListCreate, MaintenanceDetail, PerformerCreate, PerformerDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pianos/', PianoList.as_view(), name='Piano-list'),
    path('pianos/<int:id>/', PianoDetail.as_view(), name='Piano-detail'),
    path('pianos/<int:piano_id>/maintenance/', MaintenanceListCreate.as_view(), name='maintenance-list-create'),
    path('pianos/<int:piano_id>/maintenance/<int:id>', MaintenanceDetail.as_view(), name='maintenance-detail'),
    path('performer/', PerformerCreate.as_view(), name='performer-create'),
	path('performer/<int:id>/', PerformerDetail.as_view(), name='performer-detail')
]


