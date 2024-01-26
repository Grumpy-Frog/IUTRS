from django.db import models

# Create your models here.
from django.db import models
from mdeditor.fields import MDTextField

class Our_Project(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()