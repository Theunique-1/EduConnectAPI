from django.urls import path
from .views import TutorRegistrationView, TutorLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', TutorRegistrationView.as_view(), name='tutor-register'),
    path('login/', TutorLoginView.as_view(), name='tutor-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]