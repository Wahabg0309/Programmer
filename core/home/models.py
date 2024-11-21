from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    age = models.IntegerField(default=22)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()


    def __str__(self):
        return self.name


class categorie(models.Model):
    bookcategory = models.CharField(max_length=30)

    def __str__(self):
        return self.bookcategory



class book(models.Model):
    category = models.ForeignKey(categorie, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.book_name
    
