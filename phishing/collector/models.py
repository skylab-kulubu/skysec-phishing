from django.db import models

class Target(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    count = models.IntegerField(default=1)
    is_completed = models.BooleanField(default=False)