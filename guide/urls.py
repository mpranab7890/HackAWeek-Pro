from django.urls import path
from guide import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard , name= 'dashboard'),
    path('serviceform', views.setService , name = 'ServiceForm'),
    path('profile' , views.Profile , name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #git pull --rebase