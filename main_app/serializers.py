from rest_framework import serializers
from .models import Piano, MaintenanceRecord, Performer

class PianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piano
        fields = '__all__'

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
        read_only_fields = ('piano',)

class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'