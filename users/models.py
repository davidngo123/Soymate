from django.db import models
from django.contrib.auth.models import User
from PIL import Image   
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.core.files import File
import sys

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,  *args, **kwargs):
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

        super(Profile, self).save()