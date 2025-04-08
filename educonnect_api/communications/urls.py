from django.urls import path
from .views import (
    CreateMessageView,  # Create a new message
    ListMessagesView,    # List messages for the current user
    RetrieveMessageView, # Retrieve a specific message
    UpdateMessageView,   # Update an existing message
    DeleteMessageView,   # Delete a message
    SendMessageView,     # Send a message to a specific user
)

urlpatterns = [
    path('create/', CreateMessageView.as_view(), name='create-message'),
    path('list/', ListMessagesView.as_view(), name='list-messages'),
    path('<int:pk>/', RetrieveMessageView.as_view(), name='retrieve-message'),
    path('<int:pk>/update/', UpdateMessageView.as_view(), name='update-message'),
    path('<int:pk>/delete/', DeleteMessageView.as_view(), name='delete-message'),
    path('send/', SendMessageView.as_view(), name='send-message'),
]