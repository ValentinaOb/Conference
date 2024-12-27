from django.urls import path, include
#from .views import authView, home, signup, signin
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('accounts/', include('django.contrib.auth.urls')),
]