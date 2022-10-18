
from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image

from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()

class CustomUser(AbstractUser):
    # number = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

        # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height < 10 or img.width < 10:
            new_img = (10, 10)
            img.thumbnail(new_img)
            img.save(self.avatar.path)