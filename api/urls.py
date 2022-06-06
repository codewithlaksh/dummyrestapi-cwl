from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='get_routes'),
    path('get_todos/', views.get_todos, name='get_todos'),
    path('get_todo/<int:pk>/', views.get_todo, name='get_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update_todo/', views.update_todo, name='update_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo')
]
