from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    NOT_PREMIUM = 'NP'
    ONLY_PREMIUM = 'OP'
    PREMIUM_PLUS = 'PP'
    PREMIUM_CHOICES = [
        (NOT_PREMIUM, 'Not premium user'),
        (ONLY_PREMIUM, 'Only premium user'),
        (PREMIUM_PLUS, 'Premium plus user'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    is_premium = models.CharField(max_length=2, choices=PREMIUM_CHOICES, blank=True, null=True, default='NP')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)