from django.shortcuts import render
from rest_framework import viewsets
from .models import Tutors
from .serializers import TutorsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import IsTutorOrStudent
# Create your views here.

class TutorsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class TutorsViewSet(viewsets.ModelViewSet):
    queryset = Tutors.objects.all()
    serializer_class = TutorsSerializer
    pagination_class = TutorsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'expertise', 'location']
    permission_classes = [IsTutorOrStudent]