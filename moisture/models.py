from django.db import models


class MoistureLevel(models.Model):
    saturated = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
