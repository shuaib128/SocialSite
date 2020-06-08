#import modules
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


# Create models here.

#Model for profile informations
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ImageField(default='default.jpg', upload_to='profile_pics')
    coverPhoto = models.ImageField(default='default.jpg', upload_to='coverphotos')
    biodata = models.TextField(max_length=500, default='something')
    website = models.CharField(max_length=200, default='www.example.com')
    birthday = models.CharField(max_length=200, default='dd/mm/yy')
    mobile = models.CharField(max_length=200, default='00 000 000')
    facebook = models.CharField(max_length=200, default='Fb/...')
    twitter = models.CharField(max_length=200, default='Tw/...')

    def __str__(self):
        return f'{self.user.username} Profile'






#Model for post informations
class Post(models.Model):
    content = models.ImageField(upload_to='post_content')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Redirecting After making a new Post
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


