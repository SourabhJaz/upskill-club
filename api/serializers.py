from rest_framework import serializers
from .models import Category, Author, Course, Session, Concept

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'outline', 'thumbnail']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'linkedInUrl', 'outline']

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'category', 'title', 'outline', 'short_description', 'thumbnail', 'author', 'image', 'created_at']


class SessionSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    
    class Meta:
        model = Session
        fields = ['id', 'course', 'title', 'outline', 'thumbnail', 'created_at']


class ConceptSerializer(serializers.ModelSerializer):
    session = SessionSerializer(read_only=True)
    
    class Meta:
        model = Concept
        fields = ['id', 'session', 'title', 'image', 'description']
