from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import logout, login, authenticate 
from django.contrib import messages
from accounts.forms import CreateUserForm
from accounts.decorators import allowed_users
from student.models import Student

# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return redirect('admin.index')
    # else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password )
            if user is not None:
                login(request, user)
                return redirect('admin.index')
                
            else:
                messages.info(request, 'Username OR Password is incorrect')

        return render(request, 'accounts/index.html')

def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('student.index')
    # else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get("username")

                user_group = Group.objects.get(name = "student")
                user.groups.add(user_group)
                Student.objects.create(
                     user = user,
                     name = user.username,
                     email = user.email,
                     password = user.password,
                     date_joined = user.date_joined,
                )

                messages.success(request, "Account was created for " + username)
                
                return redirect('accounts.login')
        else:
            form = CreateUserForm()

        return render(request, 'accounts/register.html',context={'form':form})

def logoutUser(request):
    logout(request)
    return redirect('accounts.login')
