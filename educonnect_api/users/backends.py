from django.contrib.auth.backends import ModelBackend
from users.models import Students 
from tutors.models import Tutors

class StudentTutorBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Students.objects.get(username=username)
            if student.check_password(password) and self.user_can_authenticate(student):
                return student
        except Students.DoesNotExist:
            pass

        try:
            tutor = Tutors.objects.get(username=username)
            if tutor.check_password(password) and self.user_can_authenticate(tutor):
                return tutor
        except Tutors.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return Students.objects.get(pk=user_id)
        except Students.DoesNotExist:
            try:
                return Tutors.objects.get(pk=user_id)
            except Tutors.DoesNotExist:
                return None