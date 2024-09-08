from django.contrib import admin
from django.urls import path
from .views import (
    book_list, book_create, book_update, book_delete, index
)

urlpatterns = [
    path('', index, name='index'),
    # path('admin/', admin.site),
    path('books/', book_list, name='book_list'),
    path('books/add/', book_create, name='book_add'),
    path('books/edit/<int:pk>/', book_update, name='book_edit'),
    path('books/delete/<int:pk>/', book_delete, name='book_delete'),
]