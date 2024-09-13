from django.urls import include, path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'course', CourseReadOnlyViewSet)
router.register(r'category', CategoryReadOnlyViewSet)
router.register(r'author', AuthorReadOnlyViewSet)
router.register(r'session', SessionReadOnlyViewSet)
router.register(r'concept', ConceptReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
