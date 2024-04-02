from rest_framework import serializers
from .models import Piano

class PianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piano
        fields = '__all__'