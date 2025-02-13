"""HoqueiStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib.auth.views import LoginView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .routers import router

urlpatterns = [

    url(r'server/', include('server.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('rest/', include(router.urls)),
    path('auth/obtain/', obtain_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
    path('accounts/', include('django.contrib.auth.urls'))
]
