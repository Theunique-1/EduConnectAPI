from django.urls import path, include
from rest_framework import routers
from .views import UserRegistrationView, UserLoginView, StudentsViewSet 
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register(r'profiles', StudentsViewSet, basename='student-profile')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    
]