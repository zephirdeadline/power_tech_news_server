"""power_tech_news_server URL Configuration

The `urlpatterns` list routes URLs to views_api. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views_api
    1. Add an import:  from my_app import views_api
    2. Add a URL to urlpatterns:  path('', views_api.home, name='home')
Class-based views_api
    1. Add an import:  from other_app.views_api import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
