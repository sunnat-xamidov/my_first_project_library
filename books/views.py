from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def all_books(request):
    q = request.GET.get('q','')
    books = Book.objects.all()
    if q:
        books = books.filter(title__icontains = q)

    books = books.order_by('-created_at')

    total = books.count()

    return render(request, 'books.html', {'books': books, 'q':q, 'total':total})

def detail_book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'detail_book.html', {"book": book})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {"form": form})

def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        # Bu yerda instance=book bo'lishi shart (string emas)
        form = BookForm(request.POST, request.FILES, instance=book)  
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)

    return render(request, 'update_book.html', {"form": form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('books')
        
    return render(request, 'delete_book.html', {"book": book})

