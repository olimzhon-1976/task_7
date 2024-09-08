from django.urls import path
from .views import (
    book_list, book_create, book_update, book_delete,
    reader_list, reader_create, reader_update, reader_delete
)

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/add/', book_create, name='book_add'),
    path('books/edit/<int:pk>/', book_update, name='book_edit'),
    path('books/delete/<int:pk>/', book_delete, name='book_delete'),
    path('readers/', reader_list, name='reader_list'),
    path('readers/add/', reader_create, name='reader_add'),
    path('readers/edit/<int:pk>/', reader_update, name='reader_edit'),
    path('readers/delete/<int:pk>/', reader_delete, name='reader_delete'),
]