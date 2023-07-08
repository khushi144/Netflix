from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)
Movie_CHOICES = (
    ('seasonal','Seasonal')
    ('single', 'Single')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)
    
# Create your models here.
class Profile(models.Model):
    name = models.CharFiled(max_length=10)
    age_limit = models.CharFiled(choices=AGE_CHOICES, max_length=10)
    uuid =models.UUIDField(default=uuid.uuid4)
    
    def__str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharFiled(max_length=1000)
    description = models.TextFiled(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid =models.UUIDField(default=uuid.uuid4)
    type = models.CharFiled(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('video')
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharFiled(choices=AGE_CHOICES, max_length=10)
    
    def__str__(self):
        return self.title

class Video(models.Model):
    title = models.CharFiled(max_length=1000)
    file = models.FileField(upload_to='movies')
    
    def__str__(self):
        return title
    