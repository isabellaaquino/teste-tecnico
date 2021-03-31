from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('log/', views.logView, name='log')
] 