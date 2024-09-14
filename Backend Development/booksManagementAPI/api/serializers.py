from rest_framework import serializers
from .models import BookModel

class BookSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = BookModel
        fields = ('id', 'title', 'author', 'year', 'user')