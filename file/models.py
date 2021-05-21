"""
Models for project
"""

from django.db import models


class File(models.Model):
    """
    Models for file
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)

    objects = models.Manager()
