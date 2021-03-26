from django.db import models

# Creating model data fields for the recipe post objects 
class Post(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)


        