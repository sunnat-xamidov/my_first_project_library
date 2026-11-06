
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    image = models.ImageField(upload_to='kitoblar/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
