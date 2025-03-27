from rest_framework import permissions

class IsTutorOrStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (hasattr(request.user, 'tutors') or hasattr(request.user, 'students'))