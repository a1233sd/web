"""
URL configuration for bmstu_lab project.

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
from bmstu import views

urlpatterns = [
    path('', views.GetOrders, name='orders'),
    path('sendText', views.sendText, name='sendText'),
    path('students/', views.GetOrders, name='orders'),  # Определяем маршрут для списка студентов
    path('student/<int:id>/', views.GetOrder, name='order_detail'),  # Для детальной информации о студенте
    path('cart/', views.cart_view, name='cart'),  # Страница корзины

]