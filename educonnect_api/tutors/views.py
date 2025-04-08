from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Tutors
from .serializers import TutorRegistrationSerializer, TutorProfileSerializer, TutorLoginSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsTutorOwnerOrReadOnly
from rest_framework.routers import DefaultRouter

# Create a default router to register ViewSets
router = DefaultRouter()


# Custom pagination class for Tutors
class TutorsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100


 # ViewSet for handling CRUD operations on Tutor profiles

class TutorsViewSet(viewsets.ModelViewSet):
    queryset = Tutors.objects.all()
    serializer_class = TutorProfileSerializer
    pagination_class = TutorsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location', 'expertise']
    permission_classes = [permissions.IsAuthenticated, IsTutorOwnerOrReadOnly]


# Override get_queryset to only return the profile of the currently logged-in tutor

    def get_queryset(self):
        return Tutors.objects.filter(id=self.request.user.id)

# Override perform_update to automatically associate the updated profile with the current user
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Override perform_destroy to only allow deleting the profile of the currently logged-in tutor
    def perform_destroy(self, instance):
        if instance.id == self.request.user.id:
            instance.delete()

# Register the TutorsViewSet with the router to generate URL patterns
router.register(r'profiles', TutorsViewSet, basename='tutor-profile') # Register after definition


# View for handling tutor registration
class TutorRegistrationView(generics.CreateAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

 # Override the post method for debugging purposes (printing when the view is called)

    def post(self, request, *args, **kwargs):
        print("TutorRegistrationView post method called")
        return self.create(request, *args, **kwargs)

# View for handling tutor login and obtaining JWT tokens
class TutorLoginView(TokenObtainPairView):
    serializer_class = TutorLoginSerializer
    permission_classes = [permissions.AllowAny]