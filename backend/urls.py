from django.urls import path
from .views import main,main2

urlpatterns = [
    path('',main,name='main'),
    path('v2/',main2,name='main2'),
]