from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import TutorRegistrationSerializer, TutorProfileSerializer, TutorLoginSerializer
from .permissions import IsTutor, IsTutorOwnerOrReadOnly
from .models import Tutors
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError


# Custom pagination class for Tutors
class TutorsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# View to list all tutor profiles
class TutorListView(generics.ListAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorProfileSerializer
    pagination_class = TutorsPagination
    permission_classes = [permissions.IsAuthenticated]


# View for tutor registration
class TutorRegistrationView(generics.CreateAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# View for tutor login and obtaining JWT tokens
class TutorLoginView(TokenObtainPairView):
    serializer_class = TutorLoginSerializer
    permission_classes = (permissions.AllowAny,) 

# View for creating or updating the logged-in tutor's profile
class TutorProfileCreateView(generics.UpdateAPIView):
    serializer_class = TutorProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTutor]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save()

# View to retrieve a specific tutor's profile
class TutorProfileRetrieveView(generics.RetrieveAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTutorOwnerOrReadOnly]

# View to update a specific tutor's profile
class TutorProfileUpdateView(generics.UpdateAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTutorOwnerOrReadOnly]

# View to delete a specific tutor's profile
class TutorProfileDestroyView(generics.DestroyAPIView):
    queryset = Tutors.objects.all()
    serializer_class = TutorProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsTutorOwnerOrReadOnly]