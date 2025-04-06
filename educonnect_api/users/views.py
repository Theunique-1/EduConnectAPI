from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Students
from .serializers import UserRegistrationSerializer, StudentProfileSerializer, StudentLoginSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsStudentOwnerOrReadOnly
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 

class StudentsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentProfileSerializer
    pagination_class = StudentsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location']
    permission_classes = [permissions.IsAuthenticated, IsStudentOwnerOrReadOnly]

    def get_queryset(self):
        return Students.objects.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.id == self.request.user.id:
            instance.delete()

router.register(r'profiles', StudentsViewSet, basename='student-profile') # Register after definition

class UserRegistrationView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print("UserRegistrationView post method called")
        return self.create(request, *args, **kwargs)

class UserLoginView(TokenObtainPairView):
    serializer_class = StudentLoginSerializer
    permission_classes = [permissions.AllowAny]