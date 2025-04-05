from rest_framework import generics
from rest_framework import permissions
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer, BookingUpdateSerializer
from .permissions import IsStudentOrTutor, IsBookingOwnerOrReadOnly, IsStudentBookingOwner, IsTutorBookingOwner

class CreateBookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    permission_classes = [permissions.IsAuthenticated] # Any authenticated user can create a booking

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.students)

class ListBookingView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'students'):
            return Booking.objects.filter(student=user.students)
        elif hasattr(user, 'tutors'):
            return Booking.objects.filter(tutor=user.tutors)
        return Booking.objects.none() # Return empty queryset if user is neither student nor tutor

class UpdateBookingView(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsBookingOwnerOrReadOnly]

class DestroyBookingView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsBookingOwnerOrReadOnly]