from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete = models.CASCADE)
    pic = models.ImageField(default = 'default.jpg' , upload_to = 'profile_pics')


    def __str__(self):
        return f' Profile of { self.user.username }'



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.pic.path)

        if image.height > 300 or image.width >300:
            output_size = (300,300)
            image.thumbnail(output_size)
            image.save(self.pic.path)



