from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from .models import UserServices , Profile , Review


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.userservices.save()
        # instance.profile.save()
    except ObjectDoesNotExist:
        UserServices.objects.create(user=instance)
        # Profile.objects.create(user = instance)


@receiver(post_save, sender=User)
def create_profile1(sender, instance, created, **kwargs):
    try:
        
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user = instance)


# @receiver(post_save, sender=UserServices)
# def create_profile2(sender, instance, created, **kwargs):
#     try:
        
#         instance.review.save()
#     except ObjectDoesNotExist:
#         Review.objects.create(posts = instance)
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.userservi.save()
