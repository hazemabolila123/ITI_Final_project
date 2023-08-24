from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, related_name="student" )
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length=320)
    password = models.CharField()
    image = models.ImageField(upload_to='students/images', null=True,blank=True)
    date_joined = models.DateTimeField(null= True)
    
    def get_image_url(self):
        return f"/media/{self.image}"
