from django.urls import path, include
from .views import *

urlpatterns = [
    path('', InsertPageView, name='insertpage'), 
    path('insert/', Insertdata, name='insert')
    
]