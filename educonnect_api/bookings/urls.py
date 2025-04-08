from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListBookingView.as_view(), name='booking-list'),
    path('create/', views.CreateBookingView.as_view(), name='booking-create'),
    path('<int:pk>/', views.RetrieveBookingView.as_view(), name='booking-detail'),
    path('<int:pk>/update/', views.UpdateBookingView.as_view(), name='booking-update'),
    path('<int:pk>/delete/', views.DestroyBookingView.as_view(), name='booking-delete'),
]