"""solusi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from solusiweb import views

urlpatterns = [
    #path('studentlib/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('vice/', views.vice, name='vice'),
    path('provice/', views.provice, name='provice'),
    path('daf/', views.daf, name='daf'),
    path('studentaff/', views.studentaff, name='studentaff'),
    path('register/', views.register, name='register'),

    path('agric/', views.agric, name='agric'),
    path('commerce/', views.commerce, name='commerce'),
    path('education/', views.education, name='education'),
    path('health/', views.health, name='health'),
    path('theology/', views.theology, name='theology'),
    path('graduation/', views.graduation, name='graduation'),

    path('about/', views.about, name='about'),
    path('alumini/', views.alumini, name='alumini'),
    path('contact/', views.contact, name='contact'),
    path('library/', views.library, name='library'),
     path('studentlib/', views.studentlib, name='studentlib'),
]
