"""
URL configuration for Medical Diagnosis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Home'),
    path('booking/', include('booking.urls')),
    path('model1/', model1, name='Model1'),
    path('model2/', model2, name='Model2'),
    path('model3/', model3, name='Model3'),
    path('model4/', model4, name='Model4'),
    path('model5/', model5, name='Model5'),
    path('model6/', model6, name='Model'),
    path('model7/', model7, name='Model7'),
]
