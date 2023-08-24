from django.db import models
from student.models import Student
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    description = models.TextField(null = True, blank=True)
    image = models.ImageField(upload_to='books/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    borrowed = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL ,null=True, related_name= "books")
    return_date = models.DateField(null= True)
    # def __str__(self):
    #     return f"{self.name}"
    
    def get_image_url(self):
        return f"/media/{self.image}"
    
    def get_book_url(self):
        return f"/media/{self.book}"