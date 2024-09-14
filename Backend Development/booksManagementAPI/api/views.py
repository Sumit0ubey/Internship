from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import BookModel


def home(request):
    return render(request, 'base.html')

class Booklist(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer