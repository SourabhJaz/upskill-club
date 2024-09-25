from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from .serializers import *
from .models import *

# Create your views here.
@method_decorator(cache_control(max_age=3600), name='dispatch')
class CourseReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'id', 'author']
    search_fields = ['title']
@method_decorator(cache_control(max_age=86400), name='dispatch')
class AuthorReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['id']

@method_decorator(cache_control(max_age=86400), name='dispatch')
class CategoryReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@method_decorator(cache_control(max_age=3600), name='dispatch')
class SessionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'id', 'author']
    ordering_fields = ['created_at']

@method_decorator(cache_control(max_age=3600), name='dispatch')
class ConceptReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['session']
