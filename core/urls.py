from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('postform/', Post),
    path('bulim/<int:pk>/', bulimdata, name='bulim')
    
]


  