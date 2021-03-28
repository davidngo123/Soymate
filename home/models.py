from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image   

# Creating model data fields for the recipe post objects 

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.TextField(max_length=1500, null=False, blank=False)
    instructions = models.TextField(max_length=1500, null=False, blank=False)
    cooktime = models.IntegerField(default=10, blank=False)
    image = models.ImageField(null=False, blank = False)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-list', kwargs={'pk': self.pk})

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
        