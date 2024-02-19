from django.urls import path
from . import views

urlpatterns = [
    path('notify/', views.NotifyAPIView.as_view(), name='notify'),
    path('register_device/', views.DeviceRegistration.as_view(), name="register devices"),
    path('user/', views.UserRegistration.as_view(), name="register user"),
]