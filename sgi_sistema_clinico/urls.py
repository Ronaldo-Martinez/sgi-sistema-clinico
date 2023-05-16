"""
URL configuration for sgi_sistema_clinico project.

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
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from modulo_control.views.login import cerrar_sesion,home, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logearse/', LoginView.as_view(), name='logearse'),
    path('logout/', cerrar_sesion, name='logout'),
    path('home/', home, name='home'),
    path('control/', include('modulo_control.urls')),

]
urlpatterns += staticfiles_urlpatterns()
