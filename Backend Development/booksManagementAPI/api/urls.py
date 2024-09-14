from django.urls import path
from .views import Booklist, BookDetail, home

urlpatterns = [
    path('', home, name='home'),
    path('books/', Booklist.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
