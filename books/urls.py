from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_books, name= 'books'),
    path('detail/<int:id>/', views.detail_book, name= 'detail'),
    path('create/',views.create_book,name='create'),
    path('update/<int:id>/',views.update_book,name='update'),
    path('delete/<int:id>/',views.delete_book,name='delete'),


]