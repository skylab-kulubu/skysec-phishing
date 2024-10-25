from django.db import models

# Create your models here.

class Quiz(models.Model):
    question = models.TextField()
    opt_a = models.CharField(max_length=255)
    opt_b = models.CharField(max_length=255)
    opt_c = models.CharField(max_length=255)
    opt_d = models.CharField(max_length=255)
    true_opt = models.CharField(max_length=1,choices=[
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    ])
    is_active = models.BooleanField(default=True)



