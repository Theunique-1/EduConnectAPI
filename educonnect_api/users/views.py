from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsTutorOrStudent


# Create your views here.

class StudentsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = StudentsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email', 'location']
    permission_classes = [IsTutorOrStudent]


class UserRegistrationView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (permissions.AllowAny,)

class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)