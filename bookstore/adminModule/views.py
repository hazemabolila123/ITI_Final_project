from django.shortcuts import render,redirect, get_object_or_404
from adminModule.models import Book
from django.contrib.auth.models import User
from student.models import Student
from django.contrib.auth.decorators  import login_required
from accounts.decorators import allowed_users, admin_user

# Create your views here.
@login_required(login_url='/')
@admin_user
def index(request):
    return render(request, 'adminModule/index.html')

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def books(request):
    data_to_send = Book.objects.all()
    return render(request, 'adminModule/books.html',context={"books":data_to_send})

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def add(request):
    if request.method == "POST":
        book = Book()
        book.book_name = request.POST['book_name']
        book.author_name = request.POST['author_name']
        book.image = request.FILES['image']
        book.description = request.POST['description']
        book.borrowed = 'borrowed' in request.POST
        book.save()
        return redirect('admin.books')
    
    return render(request, 'adminModule/addbook.html')

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def edit(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.book_name = request.POST['book_name']
        book.author_name = request.POST['author_name']
        if 'image' in request.FILES:
            book.image = request.FILES['image']
        book.description = request.POST['description']
        book.borrowed = 'borrowed' in request.POST
        book.save()
        return redirect('admin.books')
    return render(request,'adminModule/editbook.html', context={"book":book})

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('admin.books')

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'adminModule/showbook.html', context={"book": book})

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def borrowed(request):
    data_to_send = Book.objects.all()
    return render(request, 'adminModule/borrowedbooks.html', context={'books':data_to_send})

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def avaliable(request):
    data_to_send = Book.objects.all()
    return render(request, 'adminModule/avaliablebooks.html', context={'books':data_to_send})

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def users(request):
    data_to_send = User.objects.all()
    return render(request, 'adminModule/users.html', context={'users':data_to_send})

@login_required(login_url='/')
@allowed_users(allowed_roles=['admin'])
def search(request): 
    if request.method == "POST":
        user = get_object_or_404(Student, id = request.POST['id'])
        return render(request, 'adminModule/showuser.html', context={"user": user})

    return render(request, 'adminModule/searchform.html')

