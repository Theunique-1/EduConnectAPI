from rest_framework.routers import DefaultRouter
from .views import TutorsViewSet

router = DefaultRouter()
router.register(r'tutors', TutorsViewSet)

urlpatterns = router.urls