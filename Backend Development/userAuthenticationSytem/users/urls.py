from django.urls import path
from .views import register, sign_up, sign_out, home

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', sign_up, name='login'),
    path('logout/', sign_out, name='logout'),
    path('', home, name='home'),
]