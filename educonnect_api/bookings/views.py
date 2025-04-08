from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer, BookingUpdateSerializer
from users.models import Students  
from tutors.models import Tutors

class ListBookingView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class CreateBookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer 

    def perform_create(self, serializer):
        student_id = self.request.data.get('student')
        tutor_id = self.request.data.get('tutor')
        try:
            student = Students.objects.get(pk=student_id)
        except Students.DoesNotExist:
            raise ValueError(f"Invalid student ID: {student_id}")
        try:
            tutor = Tutors.objects.get(pk=tutor_id)
        except Tutors.DoesNotExist:
            raise ValueError(f"Invalid tutor ID: {tutor_id}")
        serializer.save(student=student, tutor=tutor)

class RetrieveBookingView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UpdateBookingView(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer 

class DestroyBookingView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer