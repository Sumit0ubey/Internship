from django.urls import path
from .views import TodoDetail, Todolist

urlpatterns = [
    path('todos/', Todolist.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]