from django.shortcuts import render
from home.models import *
from home.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class StudentAPI(APIView):
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({"status":403,"":"Something went wrong",'error':serializer.errors})
        serializer.save()
        return Response({"":serializer.data, "":"data save successfully"})
    
    def get(self, request):
        data = student.objects.all()
        serializer = StudentSerializer(data, many = True)
        return Response(serializer.data)
    
    def patch(self, request):
        try:
            student_obj = student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data = request.data,  partial= True)
            if not serializer.is_valid():
                return Response({'status':404,'':'Something went wrong','error':serializer.errors})
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error":"Invalid id"})
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = student.objects.get(id=id)
            student_obj.delete()
            return Response({"":"Deleted"})
        except Exception as e:
            return Response({"error":"Invalid id"})
        
        
class BookAPI(APIView):
    def get(self, request):
        data = book.objects.all()
        serializer = BookSerializer(data, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({"status":403,"":"Something went wrong",'error':serializer.errors})
        serializer.save()
        return Response({"":serializer.data, "":"data save successfully"})
    
    def patch(self, request):
        student_obj = book.objects.get(id=request.data['id'])
        serializer = BookSerializer(student_obj, data = request.data,  partial= True)
        if not serializer.is_valid():
            return Response({'status':404,'':'Something went wrong','error':serializer.errors})
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request):
        id = request.GET.get('id')
        student_obj = book.objects.get(id=id)
        student_obj.delete()
        return Response({"":"Deleted"})


@api_view(['GET'])
def display_category(request):
    data = categorie.objects.all()
    serializer = CategorySerializer(data, many= True)
    return Response(serializer.data)