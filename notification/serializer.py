from rest_framework import serializers
from fcm_django.models import FCMDevice
from .models import DeviceUsers

class FCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ['id', 'registration_id', 'device_id', 'name', 'active']

class DeviceUsersSerlalizer(serializers.ModelSerializer):
    class Meta:
        model = DeviceUsers
        fields = "__all__"

