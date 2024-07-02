"""
URL configuration for honeyport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.dashboard,name="dashboard"),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('fileanalysis',views.file_analysis,name="file_analysis"),
    path('network',views.network,name="network"),
    path('photo',views.photo,name="photo"),
    path('setup',views.setup,name="setup"),
    path('server-setup',views.server_setup,name="server_setup"),
    path('start-flask-server', views.start_flask_server, name='start-flask-server'),
    path('stop-flask-server', views.stop_flask_server, name='stop-flask-server'),
    path('start-network-server', views.start_network_server, name='start_network_server'),
    path('stop-network-server', views.stop_network_server, name='stop_network_server'),
    path('network-setup', views.network_setup, name='network_setup'),
    path('Keylogger',views.Keylogger,name="Keylogger"),
    # path('setup_network/', setup_view, name='setup_view'),
    path('website',views.website,name="website")
    # path("networksetup")
    # path('dashboard',views.dashboard,name="dashboard")
]
