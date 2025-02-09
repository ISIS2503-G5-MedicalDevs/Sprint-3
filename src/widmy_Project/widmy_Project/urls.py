"""widmy_Project URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('IPS/',include('IPS.urls')),
    path('health-check/',views.healthCheck),
    path('HistoriaClinica/', include('HistoriaClinica.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]

#Descomentar el path de historias clinicas cuando se cree el modulo de historias clinicas
