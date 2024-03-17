from django.db import models


class Hr(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.TextField(default='password')
    