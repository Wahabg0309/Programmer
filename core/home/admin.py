from django.contrib import admin
from home.models import *
# Register your models here.

admin.site.register(categorie)
@admin.register(student)
class student_model(admin.ModelAdmin):
    list_display = ['name','father_name','age','email','address','phone']

@admin.register(book)
class book_model(admin.ModelAdmin):
    list_display =['category','book_name','description']