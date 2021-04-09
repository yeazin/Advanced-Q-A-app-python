from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeApp.as_view(), name= 'home' ),
    path('create_todo/', views.CreateTodoView.as_view(),name='create_todo'),
    path('edit_todo/<int:id>/',views.EditTodoView.as_view(), name='edit'),
    path('delete_todo/<int:id>', views.DeleteTodoView.as_view(), name='delete'),
    path('sign_in/', views.CreateUser.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
]