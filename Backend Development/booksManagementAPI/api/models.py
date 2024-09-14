from django.db import models
from django.contrib.auth.models import User

class BookModel(models.Model):
    title = models.CharField(max_length=280)
    author = models.CharField(max_length=250)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['year']