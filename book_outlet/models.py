from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# Create your models here.

class Book(models.Model):
   title = models.CharField(max_length=40)
   rating = models.IntegerField(
       validators=[MinValueValidator(1),MaxValueValidator(5)],)
   author = models.CharField(max_length= 40, blank=True)
   is_bestselling = models.BooleanField(default=False)


   def get_absolute_url(self):
       return reverse("book-detail", args={self.pk})
   
   def __str__(self):
       return  f"title ={self.title}, rating= {self.rating}, author= {self.author}, is_bestselling {self.is_bestselling}"