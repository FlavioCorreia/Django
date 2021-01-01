"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from .views import hello
from .views import ano
from .views import buscar_pessoa
from .views import fname2
#from .views import persons_list

from cli import urls as clients_urls

urlpatterns = [
    path('hello/', hello),
    path('admin/', admin.site.urls),
    path('ano/<int:year>/', ano),
    path('pessoa/<int:id>/', buscar_pessoa),
    path('nomes/<str:nome>/', fname2),

    path('person/', include(clients_urls)) #DE urls EM cli
]
