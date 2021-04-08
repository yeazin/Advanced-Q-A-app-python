from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeApp.as_view(), name= 'home' ),
    path('create_todo/', views.CreateTodoView.as_view(),name='create_todo')
]