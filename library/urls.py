from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
    request_book,
    add_book,
    ReaderListView,
    ReaderDetailView,
    MyProfileView,
    register,
    ReturnBookView,
)

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/request/<int:pk>/', request_book, name='request-book'),
    path('book/add/<int:pk>/', add_book, name='add-book'),
    path('readers/', ReaderListView.as_view(), name='reader-list'),
    path('readers/reader/<int:pk>', ReaderDetailView.as_view(), name='reader-detail'),
    path('login/', LoginView.as_view(next_page='book-list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='book-list'), name='logout'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('register/', register, name='register'),
    path('return-book/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]
