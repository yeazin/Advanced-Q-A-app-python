from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeApp.as_view(), name= 'home' ),
]