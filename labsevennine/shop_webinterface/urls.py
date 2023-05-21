"""labsevennine URL Configuration

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
from django.urls import path
from shop_webinterface import views

urlpatterns = [
    path('sensors/', views.sensors, name='sensors'),
    path('cameras', views.cameras, name='cameras'),
    path('monitors', views.monitors, name='monitors'),
    path('controllers', views.controllers, name='controllers'),
    path('routers', views.routers, name='routers'),
    path('Cart', views.cart, name='Cart'),
    path('ordering', views.ordering, name='ordering'),
    path('info', views.info, name='info'),
    path('search_res', views.search, name='search_res'),

]
