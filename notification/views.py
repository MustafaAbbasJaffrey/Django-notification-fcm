from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import FCMDeviceSerializer, DeviceUsersSerlalizer
from .models import DeviceUsers
from rest_framework import status
import json
from django.db.models import Q

from firebase_admin.messaging import Message
from fcm_django.models import FCMDevice

class NotifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = args[0]
        message_obj = Message(
            data={
                'title': "New User Registered",
                'body': "A new user has been registered. Check it out!",
                'icon_url': "icon",
                'url': "https://google.com",        
            }  
        )
        devices = FCMDevice.objects.filter(user_id=user_id)
        print(devices)
        devices.send_message(message_obj)
        return Response("Notification sent to all")
    
    
class DeviceRegistration(CreateAPIView):
    queryset = FCMDevice.objects.all()
    serializer_class = FCMDeviceSerializer

class UserRegistration(ListCreateAPIView):
    queryset = DeviceUsers.objects.all()
    serializer_class = DeviceUsersSerlalizer

    def perform_create(self, serializer):
        super().perform_create(serializer)

        client_data = self.request.data

        if not FCMDevice.objects.filter(user_id=client_data.get('user_id')):
            device = FCMDevice(registration_id = client_data.get('registration_id'), user_id = client_data.get('user_id'))
            device.save()

        notify_view = NotifyAPIView()
        notify_view.post(self.request, client_data.get('user_id'))

