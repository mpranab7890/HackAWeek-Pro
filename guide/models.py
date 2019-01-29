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
    name_of_service = models.CharField(default = 'Unknown',max_length=50)
    location = models.CharField(max_length = 100)
    type_of_service = models.CharField(blank = False , max_length=50)
    details = models.TextField()
    image= models.ImageField( upload_to='service_pics')



    def __str__(self):
        return self.name_of_service

    


# Create your models here.
