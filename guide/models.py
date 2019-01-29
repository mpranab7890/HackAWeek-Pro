from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField( max_length=254)
#     country = models.CharField( max_length=50)

class UserServices (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name_of_service = models.CharField(max_length=50)
    location = models.CharField(max_length = 100)
    type_of_service = models.CharField(blank = False , max_length=50)
    details = models.TextField()
    image= models.ImageField( upload_to='service_pics')



    def __str__(self):
        return f'{self.user.username}:{self.name_of_service}'


class Profile(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default ='profile_pics/default.jpg',upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# Create your models here.
