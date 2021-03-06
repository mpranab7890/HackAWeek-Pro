"""Pauna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from guide import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , views.home , name='index' ),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='guide/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='guide/index.html'),name='logout'),
    path('dashboard/',include('guide.urls')),
    path('posts/<int:pk>/' , views.DetailView, name = 'posts'),
    path('posts/<int:pk>/book' , views.bookView, name = 'book'),
    path('homestay/' , views.homestayView , name='homestay'),
    path('transport/' , views.transportView , name='transport'),
    path('hotel/' , views.hotelView , name='hotel'),
    path('travel/' , views.travelagencyView , name='travel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
