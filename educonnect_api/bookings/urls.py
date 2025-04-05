from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.ListBookingView.as_view(), name='booking-list'),
    path('bookings/create/', views.CreateBookingView.as_view(), name='booking-create'),
    path('bookings/<int:pk>/', views.UpdateBookingView.as_view(), name='booking-detail'),
    path('bookings/<int:pk>/delete/', views.DestroyBookingView.as_view(), name='booking-delete'),
]