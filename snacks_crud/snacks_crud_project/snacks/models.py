from django.db import models
from django.contrib.auth.models import User

class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
