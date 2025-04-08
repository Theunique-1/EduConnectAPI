from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsSenderOrReadOnly
from django.db.models import Q
from users.models import Students
from tutors.models import Tutors

class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'students'):
            serializer.save(sender_student=user.students)
        elif hasattr(user, 'tutors'):
            serializer.save(sender_tutor=user.tutors)
        else:
            raise serializers.ValidationError("User must be a student or a tutor to send a message.")

class ListMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'students'):
            return Message.objects.filter(Q(sender_student=user.students) | Q(recipient_student=user.students)).order_by('-timestamp')
        elif hasattr(user, 'tutors'):
            return Message.objects.filter(Q(sender_tutor=user.tutors) | Q(recipient_tutor=user.tutors)).order_by('-timestamp')
        return Message.objects.none()

class RetrieveMessageView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'students'):
            return Message.objects.filter(Q(sender_student=user.students) | Q(recipient_student=user.students))
        elif hasattr(user, 'tutors'):
            return Message.objects.filter(Q(sender_tutor=user.tutors) | Q(recipient_tutor=user.tutors))
        return Message.objects.none()

class UpdateMessageView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'students'):
            return Message.objects.filter(sender_student=user.students)
        elif hasattr(user, 'tutors'):
            return Message.objects.filter(sender_tutor=user.tutors)
        return Message.objects.none()

class DeleteMessageView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'students'):
            return Message.objects.filter(sender_student=user.students)
        elif hasattr(user, 'tutors'):
            return Message.objects.filter(sender_tutor=user.tutors)
        return Message.objects.none()

class SendMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        recipient_username = self.request.data.get('recipient_username')
        recipient_type = self.request.data.get('recipient_type')
        self._set_message_sender(serializer, user)
        recipient = self._get_message_recipient(recipient_username, recipient_type)
        if recipient:
            if isinstance(recipient, Students):
                serializer.save(recipient_student=recipient)
            elif isinstance(recipient, Tutors):
                serializer.save(recipient_tutor=recipient)
            else:
                raise serializers.ValidationError("Invalid recipient type.")
        else:
            raise serializers.ValidationError(f"Recipient '{recipient_username}' not found.")

    def _set_message_sender(self, serializer, user):
        if hasattr(user, 'students'):
            serializer.save(sender_student=user.students)
        elif hasattr(user, 'tutors'):
            serializer.save(sender_tutor=user.tutors)
        else:
            raise serializers.ValidationError("User must be a student or a tutor.")

    def _get_message_recipient(self, username, r_type):
        try:
            if r_type == 'student':
                return Students.objects.get(username=username)
            elif r_type == 'tutor':
                return Tutors.objects.get(username=username)
            return None
        except (Students.DoesNotExist, Tutors.DoesNotExist):
            return None