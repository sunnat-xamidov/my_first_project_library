from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title","context","image"]

        labels = {"title":"Kitob nomi", "context":"Kitob haqida", "image":"rasmi"}

    def clean_data(self):
        title = self.clean_data['title'].strip()
        if len(title) > 3:
            raise forms.ValidationError("Kitob nomi kamida 3ta belgidan iborat bo'lishi kerak")
        return title