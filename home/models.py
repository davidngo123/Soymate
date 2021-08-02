from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image   
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.core.files import File
import sys

# Creating model data fields for the recipe post objects 

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name
#for recipes
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    ingredients = models.TextField(max_length=1500, null=False, blank=False)
    instructions = models.TextField(max_length=1500, null=False, blank=False)
    cooktime = models.IntegerField(default=10, blank=False)
    image = models.ImageField(null=False, blank = False)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-list', kwargs={'pk': self.pk})

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()
        if im.height > 400 or im.width > 400:
        # Resize/modify the image
            im = im.resize((400, 400))

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=95)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                            sys.getsizeof(output), None)

        super(Post, self).save()