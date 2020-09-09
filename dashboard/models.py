from django.db import models
from django.contrib.auth.models import User

class subjects(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title