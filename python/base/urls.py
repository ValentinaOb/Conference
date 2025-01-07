from . import views
from django.urls import path

urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('speaker/', views.speaker, name='speaker'),
    path('schedule/', views.schedule, name='schedule'),
    path('contact/', views.contact, name='contact'),
    
    path('sign/', views.sign, name='sign'),
    
    path('home/', views.base, name='home'),
]