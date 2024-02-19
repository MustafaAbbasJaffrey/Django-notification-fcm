from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db import models


class DeviceUsers(User):
    pass
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)