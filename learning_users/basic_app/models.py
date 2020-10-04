from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #to add additional fields to existing User model
    user = models.OneToOneField(User)
    #additional fields:
    portfolio_site = models.URLField(blank=True) #user does not need to fill this field
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username
