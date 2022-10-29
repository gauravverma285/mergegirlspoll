
from enum import unique
from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image
from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField
# from django.contrib.auth import get_user_model
# User = get_user_model()

class CustomUser(AbstractUser):
    # number = models.IntegerField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_images')
    country = models.CharField(max_length=10)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    text = models.TextField()
    image = models.ImageField(upload_to='feature_image')
    thumbnail_image = models.ImageField(upload_to='thumbnail_image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
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


class Comment(models.Model): 
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, related_name='reply')

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 


class ReplyComment(models.Model):
   reply_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
   replier_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   reply_content = models.TextField()
   replied_date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return "'{}' replied with '{}' to '{}'".format(self.replier_name,self.reply_content, self.reply_comment)