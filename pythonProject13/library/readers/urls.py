from django.urls import path
from .views import (
    reader_list, reader_create, reader_update, reader_delete
)

urlpatterns = [
    path('readers/', reader_list, name='reader_list'),
    path('readers/add/', reader_create, name='reader_add'),
    path('readers/edit/<int:pk>/', reader_update, name='reader_edit'),
    path('readers/delete/<int:pk>/', reader_delete, name='reader_delete'),
]