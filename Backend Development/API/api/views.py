from rest_framework import generics
from .permissions import isOwnerOnly
from .serializers import Todoserializer
from todo.models import Task

from rest_framework.pagination import CursorPagination
class TodoCursorPagination(CursorPagination):
    ordering = 'id'
    page_size = 2

class Todolist(generics.ListCreateAPIView):
    pagination_class = TodoCursorPagination
    permission_classes = (isOwnerOnly,)
    queryset = Task.objects.all()
    serializer_class = Todoserializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOnly,)
    queryset = Task.objects.all()
    serializer_class = Todoserializer