from django.contrib import admin
from .models import UserServices,Profile,Review
# Register your models here.
admin.site.register(UserServices)
admin.site.register(Profile)
admin.site.register(Review)