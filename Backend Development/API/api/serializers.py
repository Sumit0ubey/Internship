from rest_framework import serializers
from .models import Task

class Todoserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'completed', 'user')

