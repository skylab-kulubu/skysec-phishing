from django.db import models
from accounts.models import User


class Target(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    count = models.IntegerField(default=1)
    is_completed = models.BooleanField(default=False)