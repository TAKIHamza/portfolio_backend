from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    SkillViewSet,
    ContactSubmissionViewSet,
    ProjectImageViewSet  # Make sure to import the new ViewSet
)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact', ContactSubmissionViewSet)


# Add this after the other registrations
router.register(r'projects/(?P<project_pk>[^/.]+)/images', ProjectImageViewSet, basename='projectimages')

urlpatterns = [
    path('', include(router.urls)),
]
