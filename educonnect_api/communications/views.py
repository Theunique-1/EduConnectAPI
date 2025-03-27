from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class MessagesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessagesPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'receiver', 'is_read']