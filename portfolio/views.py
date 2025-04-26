from portfolio_backend import settings
from rest_framework import viewsets, permissions
from .models import Profile, Project, ProjectImage, Skill, ContactSubmission
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    SkillSerializer,
    ContactSubmissionSerializer,
    ProjectImageSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware.csrf import get_token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator # type: ignore

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = []  # Disable authentication for this view
    permission_classes = []     # Disable permission checks

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'error': 'Email and password required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is None:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({
            'user': {
                'id': user.id,
                'email': user.email,
                'is_admin': user.is_superuser
            },
            'access_token': access_token,
        }, status=status.HTTP_200_OK)

        # Set cookies
        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=settings.SECURE_SSL_REDIRECT if not settings.DEBUG else False,
            samesite='Lax',
            max_age=60 * 60 * 24 * 7  # 7 days
        )

        # Set CSRF token
        response.set_cookie(
            'csrftoken',
            get_token(request),
            httponly=False,
            secure=settings.SECURE_SSL_REDIRECT if not settings.DEBUG else False,
            samesite='Lax'
        )

        return response
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response(
            {'message': 'Successfully logged out'},
            status=status.HTTP_200_OK
        )
        
        # Clear refresh token cookie
        response.delete_cookie('refresh_token')
        return response
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

# Add this new ViewSet
class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(project_id=self.kwargs['project_pk'])

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]