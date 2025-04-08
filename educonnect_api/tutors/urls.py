from django.urls import path, include
from rest_framework import routers
from .views import TutorRegistrationView, TutorLoginView, TutorsViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register(r'profiles', TutorsViewSet, basename='tutor-profile')

urlpatterns = [
    path('register/', TutorRegistrationView.as_view(), name='tutor-register'),
    path('login/', TutorLoginView.as_view(), name='tutor-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]