from django.urls import path, include
from .views import *

urlpatterns = [
    path('', InsertPageView, name='insertpage'), 
    path('insert/', Insertdata, name='insert'),
    path('showpage/', ShowPage, name='showpage'),
    path('editpage/<int:pk>', EditPage, name='editpage'),
    path('Update/<int:pk>', UpdateData, name='Update')
]