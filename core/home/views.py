from django.shortcuts import render
from home.models import *
from home.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def home(request):
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({"status":403,"":"Something went wrong",'error':serializer.errors})
    serializer.save()
    return Response({"":serializer.data, "":"data save successfully"})


@api_view(['GET'])
def display(request):
    data = student.objects.all()
    serializer = StudentSerializer(data, many = True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update(request, id):
    student_obj = student.objects.get(id=id)
    serializer = StudentSerializer(student_obj, data = request.data,  partial= True)
    if not serializer.is_valid():
        return Response({'status':404,'':'Something went wrong','error':serializer.errors})
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    student_obj = student.objects.get(id=id)
    student_obj.delete()
    return Response({"":"Deleted"})


@api_view(['POST'])
def book_post(request):
    serializer = BookSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({"status":403,"":"Something went wrong",'error':serializer.errors})
    serializer.save()
    return Response({"":serializer.data, "":"data save successfully"})


@api_view(['GET'])
def display_book(request):
    data = book.objects.all()
    serializer = BookSerializer(data, many = True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_book(request, id):
    student_obj = book.objects.get(id=id)
    serializer = BookSerializer(student_obj, data = request.data,  partial= True)
    if not serializer.is_valid():
        return Response({'status':404,'':'Something went wrong','error':serializer.errors})
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_book(request, id):
    student_obj = book.objects.get(id=id)
    student_obj.delete()
    return Response({"":"Deleted"})

@api_view(['GET'])
def display_category(request):
    data = categorie.objects.all()
    serializer = CategorySerializer(data, many= True)
    return Response(serializer.data)