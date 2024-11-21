from home.models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = '__all__'
    def validate(self, data):
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({"error":"Name can't be numeric"})
        if data['father_name']:
            for i in data['father_name']:
                if i.isdigit():
                    raise serializers.ValidationError({"error":"Father name can't be numeric"})
        if data['phone']:
            for i in data['phone']:
                if i.isalpha():
                    raise serializers.ValidationError({"error":"Phone can't be alphabets"})
        if data['age'] < 18:
                raise serializers.ValidationError({"":"Age must be >= 18"})
                return data


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = categorie
        exclude = ['id']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = book
        fields = '__all__'