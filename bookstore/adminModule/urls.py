from django.urls import path, include
from adminModule.views import index, books, add,edit, delete, show, borrowed, avaliable, users, search
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', index, name='admin.index'),
    path('books', books, name='admin.books'),
    path('addbooks', add, name='admin.addbook'),
    path('editbook/<int:id>', edit, name='admin.editbook'),
    path('deletebook/<int:id>', delete, name='admin.deletebook'),
    path('showbook/<int:id>', show, name='admin.showbook'),
    path('showborrowedbook', borrowed, name='admin.borrowedbook'),
    path('showavailablebook', avaliable, name='admin.avaliablebook'),
    path('showusers', users, name='admin.users'),
    path('search', search, name='admin.search' ),
    path('password/', auth_view.PasswordChangeView.as_view(), name='admin.password'),
    path('', include('django.contrib.auth.urls'))
]