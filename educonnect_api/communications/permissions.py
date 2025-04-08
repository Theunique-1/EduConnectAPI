from rest_framework import permissions

class IsSenderOrReadOnly(permissions.BasePermission):
    """
    Object-level permission: sender can edit/delete, participants can read.
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        is_sender = False
        is_recipient = False

        if hasattr(user, 'students'):
            is_sender = obj.sender_student == user.students
            is_recipient = obj.recipient_student == user.students
        elif hasattr(user, 'tutors'):
            is_sender = obj.sender_tutor == user.tutors
            is_recipient = obj.recipient_tutor == user.tutors

        if request.method in permissions.SAFE_METHODS:
            return is_sender or is_recipient
        return is_sender