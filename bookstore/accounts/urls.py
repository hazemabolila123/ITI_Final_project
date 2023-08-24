from django.urls import path
from accounts.views import index,registerPage, logoutUser

urlpatterns = [
    path('', index, name='accounts.login'),
    path('register', registerPage, name='accounts.register'),
    path('logout', logoutUser, name='accounts.logout')
]