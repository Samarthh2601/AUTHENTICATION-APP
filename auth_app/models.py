from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class EUser(User):
    phone_number = models.CharField(max_length=15)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)