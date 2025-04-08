from rest_framework import permissions


# Custom permission to check if the requesting user is a Tutor
class IsTutor(permissions.BasePermission):
    # Check if the user is authenticated and is an instance of the Tutors model
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'tutors')

# Custom permission to allow only the owner of a Tutor object to edit or delete it
class IsTutorOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id  # 'obj' is a Tutors instance, and the owner is the tutor themselves.