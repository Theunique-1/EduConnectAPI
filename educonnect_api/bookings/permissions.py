from rest_framework import permissions

class IsStudentOrTutor(permissions.BasePermission):
    """
    Custom permission to allow only students or tutors to access booking related views.
    """
    def has_permission(self, request, view):
        return request.user and (
            hasattr(request.user, 'students') or hasattr(request.user, 'tutors')
        )

class IsBookingOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of a booking to edit it.
    Read-only access is allowed to anyone.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the student or tutor of the booking.
        return obj.student == request.user.students or obj.tutor == request.user.tutors

class IsStudentBookingOwner(permissions.BasePermission):
    """
    Custom permission to allow only the student who created the booking to access.
    """
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user.students

class IsTutorBookingOwner(permissions.BasePermission):
    """
    Custom permission to allow only the tutor associated with the booking to access.
    """
    def has_object_permission(self, request, view, obj):
        return obj.tutor == request.user.tutors