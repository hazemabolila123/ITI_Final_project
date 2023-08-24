from django.shortcuts import render, get_object_or_404, redirect
from adminModule.models import Book
from student.models import Student
from django.contrib.auth.decorators  import login_required
from accounts.decorators import allowed_users
import datetime
# Create your views here.
@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def index(request):
    return render(request, 'student/index.html')

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def books(request):
    data_to_send = Book.objects.all()
    return render(request, 'student/books.html',context={"books":data_to_send})

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'student/showbook.html', context={"book": book})

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def borrow(request, id):
    book = get_object_or_404(Book, id=id)
    if book.borrowed == False:
        if request.method == "POST":
            book.borrowed = True
            book.student = request.user.student
            book.return_date = datetime.date.today() + datetime.timedelta(days=14)
            book.save()
            return redirect('student.index')
        return render(request, 'student/borrowbook.html', context={"book": book})
    else:
        return render(request, 'student/alreadyborrowed.html')

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def info(request):
    student = request.user.student
    if request.method == "POST":
        if 'image' in request.FILES:
            student.image = request.FILES['image']
        student.save()
        return redirect('student.index')

    return render(request, 'student/info.html', context={"student":student})

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def readinglist(request):
    student = request.user.student
    return render(request, 'student/readinglist.html', context={"student":student})


@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def returnbtn(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.borrowed = False
        book.student = None
        book.return_date = None
        book.save()
        return redirect('student.index')
    return render(request, 'student/returnform.html', context={"book": book})

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def search(request): 
    if request.method == "POST":
        book = get_object_or_404(Book, book_name = request.POST['name'])
        return render(request, 'student/showbook.html', context={"book": book})

    return render(request, 'student/searchform.html')

@login_required(login_url='/')
@allowed_users(allowed_roles=['student'])
def avaliable(request):
    data_to_send = Book.objects.all()
    return render(request, 'student/avaliablebooks.html', context={'books':data_to_send})
