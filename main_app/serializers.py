from rest_framework import serializers
from .models import Piano, MaintenanceRecord, Performer
from django.contrib.auth.models import User # add this line to list of imports

# include User serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username','email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
    
        return user

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
        read_only_fields = ('piano',)


class PerformerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Performer
        fields = '__all__'


class PianoSerializer(serializers.ModelSerializer):
    performer = PerformerSerializer(many=True, read_only=True)

    class Meta:
        model = Piano
        fields = '__all__'  # or specify fields explicitly