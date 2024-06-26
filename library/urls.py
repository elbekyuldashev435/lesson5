from django.urls import path
from .views import get_info, get_books, get_detail


urlpatterns = [
    path('', get_info, name='get_info'),
    path('books/<int:pk>', get_books, name='get_books'),
    path('books/detail/<int:pk>', get_detail, name='get_detail'),
]