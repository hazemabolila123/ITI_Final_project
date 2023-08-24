from django.urls import path, include
from student.views import index,books, show, borrow, info,readinglist, returnbtn, search, avaliable
from django.contrib.auth import views as auth_view

urlpatterns = [
   path('', index, name='student.index'),
   path('books', books, name='student.books'),
   path('showbook/<int:id>', show, name='student.showbook'),
   path('borrowbook/<int:id>', borrow, name='student.borrow'),
   path('info', info, name='student.info'),
   path('readinglist', readinglist, name='student.readinglist'),
   path('returnform/<int:id>', returnbtn, name='student.returnform'),
   path('search', search, name='student.search' ),
   path('password/', auth_view.PasswordChangeView.as_view(), name='student.password'),
   path('', include('django.contrib.auth.urls')),
   path('avaliablebooks', avaliable, name='student.avaliable' )
] 