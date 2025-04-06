from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Students
from .serializers import UserRegistrationSerializer, StudentProfileSerializer, StudentLoginSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsStudentOwnerOrReadOnly
from rest_framework.routers import DefaultRouter

# Create a default router to register ViewSets

router = DefaultRouter() 


# Custom pagination class for Students

class StudentsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


 # ViewSet for handling CRUD operations on Student profiles   

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentProfileSerializer
    pagination_class = StudentsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']
    permission_classes = [permissions.IsAuthenticated, IsStudentOwnerOrReadOnly]


# Override get_queryset to only return the profile of the currently logged-in user

    def get_queryset(self):
        return Students.objects.filter(id=self.request.user.id)

# Override perform_update to automatically associate the updated profile with the current user
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Override perform_destroy to only allow deleting the profile of the currently logged-in user
    def perform_destroy(self, instance):
        if instance.id == self.request.user.id:
            instance.delete()

# Register the StudentsViewSet with the router to generate URL patterns

router.register(r'profiles', StudentsViewSet, basename='student-profile') # Register after definition


# View for handling user registration
class UserRegistrationView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

 # Override the post method for debugging purposes (printing when the view is called)   

    def post(self, request, *args, **kwargs):
        print("UserRegistrationView post method called")
        return self.create(request, *args, **kwargs)

# View for handling user login and obtaining JWT tokens
class UserLoginView(TokenObtainPairView):
    serializer_class = StudentLoginSerializer
    permission_classes = [permissions.AllowAny]