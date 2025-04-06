# EduConnectAPI - Connecting Students and Tutors
A Django REST Framework API  to facilitate connections between students and tutors, including user authentication, booking management and messaging.

## Overview

The EduConnect API is a Django REST Framework backend designed to facilitate connections between students and tutors. It provides functionalities for user authentication (registration and login for both students and tutors), managing student and tutor profiles, handling booking requests, and enabling communication between users.



## Features

Here's a breakdown of the key features and how they work:

### 1. User Management (`users` app)

* **Student Registration:** New students can create accounts.
* **Student Login:** Registered students can log in to obtain access and refresh tokens.
* **Student Profile Management:** Students can view, update, and (soft) delete their profiles.
    * **How it works:** The `/api/users/profiles/` endpoint (using a ViewSet) allows CRUD operations on student profiles. Authentication via JWT is required for these operations.

### 2. Tutor Management (`tutors` app)

* **Tutor Registration:** Prospective tutors can register.
* **Tutor Login:** Registered tutors can log in to obtain access and refresh tokens.
* **Tutor Profile Management:** Tutors can create, view, update, and delete their profiles.
    * **How it works:** The `/api/tutors/profiles/` endpoint handles CRUD operations for tutor profiles. JWT authentication is required.

### 3. Booking Management (`bookings` app)

* **Creating Bookings:** Authenticated students can create booking requests with tutors.
    * **How it works:** A POST request to `/api/bookings/create/` with the `student`, `tutor` (using their IDs), `date_time`, `duration`, `is_online`, and `location` will create a new booking record.
* **Listing Bookings:** Authenticated users can view their bookings.
    * **How it works:** A GET request to `/api/bookings/` will return a list of bookings.
* **Viewing Booking Details:** Users can retrieve specific booking information.
    * **How it works:** A GET request to `/api/bookings/{booking_id}/` will return the details of the specified booking.
* **Updating Booking Status:** Authorized users can update booking details and status.
    * **How it works:** A PUT or PATCH request to `/api/bookings/{booking_id}/` with updated fields in the request body will modify the booking.
* **Deleting Bookings:** Users might be able to cancel bookings.
    * **How it works:** A DELETE request to `/api/bookings/{booking_id}/delete/` will remove the specified booking.

### 4. Communication Management (`communications` app)

* **Sending Messages:** Authenticated users can send messages to each other.
    * **How it works:** A POST request to `/api/communications/messages/` with `sender`, `receiver`, and `content` will send a new message. The `sender` and `receiver` should correspond to either a student or a tutor user ID.
* **Listing Messages:** Authenticated users can view their messages.
    * **How it works:** A GET request to `/api/communications/messages/` will return a list of messages. You might need to implement filtering to view specific conversations.
* **Viewing Message Details:** Users can retrieve specific message information.
    * **How it works:** A GET request to `/api/communications/messages/{message_id}/` will return the details of the specified message.

## Getting Started

### Prerequisites

* **Python:** Make sure you have Python 3.x installed.
* **pip:** Python package installer.
* **Virtual Environment (recommended):** To isolate project dependencies.

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone [repository_url]
    cd educonnect_api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure you have a `requirements.txt` file. If not, run `pip freeze > requirements.txt` after installing necessary packages.)*

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be accessible at `http://127.0.0.1:8000/api/`.

## Testing API Endpoints (CRUD Operations with Examples)

You can use tools like [Postman](https://www.postman.com/) or `curl` to test the API endpoints. Remember to replace placeholder IDs and data with your actual values and include the `Authorization: Bearer [your_access_token]` header for protected endpoints.

**Base URL:** `http://127.0.0.1:8000/api/`

### 1. Users (`users` app)

#### Registration (Create)

**Endpoint:** `/api/users/register/`
**Method:** `POST`
**Headers:** `Content-Type: application/json`
**Body (Raw - JSON):**

```json
{
    "username": "student1",
    "email": "student1@gmail.com",
    "password": "password123",
    "first_name": "Test",
    "last_name": "Student",
    "bio": "Eager to learn!",
    "location": "Nigeria"
}
Expected Response (Success - HTTP 201 Created): A successful registration will return a 201 Created status code. The response body might be empty or contain user details.

Login (Retrieve Token)
Endpoint: /api/users/login/
Method: POST
Headers: Content-Type: application/json
Body (Raw - JSON):

JSON

{
    "username": "student1",
    "password": "password123"
}
Expected Response (Success - HTTP 200 OK):

JSON

{
    "refresh": "...",
    "access": "..."
}
You'll need the access token for subsequent requests to protected endpoints. Include it in the Authorization header as Bearer [your_access_token].

Retrieve Student Profile (Read - GET)
Endpoint: /api/users/profiles/{student_id}/ (Replace {student_id} with the actual ID of a student)
Method: GET
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 200 OK):

JSON

{
    "profile_picture": null,
    "bio": "Eager to learn!",
    "location": "Nigeria",
    "id": 1,
    "username": "student1",
    "email": "[student1@gmail.com]",
    "first_name": "Test",
    "last_name": "Student"
}
Update Student Profile (Update - PUT/PATCH)
Endpoint: /api/users/profiles/{student_id}/
Method: PUT or PATCH
Headers: Content-Type: application/json, Authorization: Bearer [your_access_token]
Body (Raw - JSON):

JSON

{
    "bio": "Currently learning advanced topics",
    "location": "OWEERI"
}
Expected Response (Success - HTTP 200 OK): Returns the updated student profile.

Delete Student Profile (Delete - DELETE)
Endpoint: /api/users/profiles/{student_id}/
Method: DELETE
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 204 No Content): An empty response with a 204 No Content status code.


TUTORS APP ENDPOINTS

2. Tutors (tutors app)
Tutor Registration (Create)
Endpoint: /api/tutors/register/
Method: POST
Headers: Content-Type: application/json
Body (Raw - JSON):

JSON

{
    "username": "tutor1",
    "email": "tutor1@gmail.com",
    "password": "password123",
    "first_name": "Test",
    "last_name": "Tutor"
}
Expected Response (Success - HTTP 201 Created): A 201 Created status code.

Tutor Login (Retrieve Token)
Endpoint: /api/tutors/login/
Method: POST
Headers: Content-Type: application/json
Body (Raw - JSON):

JSON

{
    "username": "tutor1",
    "password": "password123"
}
Expected Response (Success - HTTP 200 OK): Returns access and refresh tokens.

Create Tutor Profile (Create - POST)
Endpoint: /api/tutors/profiles/
Method: POST
Headers: Content-Type: application/json, Authorization: Bearer [your_access_token]
Body (Raw - JSON):

JSON

{
    "expertise": "Mathematics, Physics",
    "hourly_rate": 30.00,
    "online_availability": "Monday-Friday Evenings",
    "in_person_availability": "Saturday Mornings",
    "location": "Nigeria"
}
Expected Response (Success - HTTP 201 Created): Returns the details of the newly created tutor profile.

List Tutor Profiles (Read - GET)
Endpoint: /api/tutors/profiles/
Method: GET
Headers: (Optional: Authorization: Bearer [your_access_token])

Expected Response (Success - HTTP 200 OK): Returns a list of tutor profile objects.

Retrieve Tutor Profile (Read - GET)
Endpoint: /api/tutors/profiles/{tutor_id}/ (Replace {tutor_id} with the actual ID)
Method: GET
Headers: (Optional: Authorization: Bearer [your_access_token])

Expected Response (Success - HTTP 200 OK): Returns the details of the specific tutor profile.

Update Tutor Profile (Update - PUT/PATCH)
Endpoint: /api/tutors/profiles/{tutor_id}/
Method: PUT or PATCH
Headers: Content-Type: application/json, Authorization: Bearer [your_access_token]
Body (Raw - JSON):

JSON

{
    "hourly_rate": 35.00,
    "online_availability": "Daily Evenings"
}
Expected Response (Success - HTTP 200 OK): Returns the updated tutor profile details.

Delete Tutor Profile (Delete - DELETE)
Endpoint: /api/tutors/profiles/{tutor_id}/
Method: DELETE
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 204 No Content): An empty response with a 204 No Content status code.

3. Bookings (bookings app)
Create Booking (Create - POST)
Endpoint: /api/bookings/create/
Method: POST
Headers: Content-Type: application/json, Authorization: Bearer [your_access_token]
Body (Raw - JSON - Example):

JSON

{
    "student": 1,  // Replace with an existing student ID
    "tutor": 2,    // Replace with an existing tutor ID
    "date_time": "2025-04-15T10:00:00Z",
    "duration": 90,
    "is_online": true,
    "location": "Online"
}
Expected Response (Success - HTTP 201 Created): Returns the details of the newly created booking, including nested student and tutor information.

JSON

{
    "id": 1,
    "student": {
        "id": 1,
        "username": "teststudent"
    },
    "student_id": 1,
    "tutor": {
        "id": 2,
        "username": "testtutor"
    },
    "tutor_id": 2,
    "date_time": "2025-04-15T10:00:00Z",
    "duration": 90,
    "is_online": true,
    "location": "Online",
    "booking_status": "PENDING",
    "created_at": "2025-04-06T19:20:00.000Z",
    "updated_at": "2025-04-06T19:20:00.000Z"
}
List Bookings (Read - GET)
Endpoint: /api/bookings/
Method: GET
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 200 OK): Returns a list of booking objects.

JSON

[
    {
        "id": 1,
        "student": {
            "id": 1,
            "username": "teststudent"
        },
        "student_id": 1,
        "tutor": {
            "id": 2,
            "username": "testtutor"
        },
        "tutor_id": 2,
        "date_time": "2025-04-15T10:00:00Z",
        "duration": 90,
        "is_online": true,
        "location": "Online",
        "booking_status": "PENDING",
        "created_at": "2025-04-06T19:20:00.000Z",
        "updated_at": "2025-04-06T19:20:00.000Z"
    },
    // ... more bookings
]
Retrieve Booking (Read - GET)
Endpoint: /api/bookings/{booking_id}/ (Replace {booking_id} with the actual ID)
Method: GET
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 200 OK): Returns the details of the specific booking.

JSON

{
    "id": 1,
    "student": {
        "id": 1,
        "username": "teststudent"
    },
    "student_id": 1,
    "tutor": {
        "id": 2,
        "username": "testtutor"
    },
    "tutor_id": 2,
    "date_time": "2025-04-15T10:00:00Z",
    "duration": 90,
    "is_online": true,
    "location": "Online",
    "booking_status": "PENDING",
    "created_at": "2025-04-06T19:20:00.000Z",
    "updated_at": "2025-04-06T19:20:00.000Z"
}
Update Booking (Update - PUT/PATCH)
Endpoint: /api/bookings/{booking_id}/
Method: PUT or PATCH
Headers: Content-Type: application/json, Authorization: Bearer [your_access_token]
Body (Raw - JSON - Example):

JSON

{
    "date_time": "2025-04-16T14:00:00Z",
    "booking_status": "CONFIRMED"
}
Expected Response (Success - HTTP 200 OK): Returns the updated booking details.

JSON

{
    "id": 1,
    "student": {
        "id": 1,
        "username": "teststudent"
    },
    "student_id": 1,
    "tutor": {
        "id": 2,
        "username": "testtutor"
    },
    "tutor_id": 2,
    "date_time": "2025-04-16T14:00:00


Delete Booking (Delete - DELETE)

**Endpoint:** `/api/bookings/{booking_id}/delete/` (Replace `{booking_id}` with the actual ID)
**Method:** `DELETE`
**Headers:** `Authorization: Bearer [your_access_token]`
**Body:** (No request body is typically required for a DELETE operation)

**Expected Response (Success - HTTP 204 No Content):** An empty response with a `204 No Content` status code.



### 4. Communication Management (`communications` app)

#### Send Message (Create - POST)

**Endpoint:** `/api/communications/messages/`
**Method:** `POST`
**Headers:** `Content-Type: application/json`, `Authorization: Bearer [your_access_token]`
**Body (Raw - JSON - Example - Assuming IDs 1 and 2 are existing users):**

```json
{
    "sender": 1,     // ID of the sending user (student or tutor)
    "receiver": 2,   // ID of the receiving user
    "content": "Hello, are you available tomorrow?"
}
Expected Response (Success - HTTP 201 Created): Returns the details of the newly created message, including nested sender and receiver information (if your viewset is configured to do so).

JSON

{
    "id": 1,
    "sender": 1,
    "sender_student": {
        "id": 1,
        "profile_picture": null,
        "bio": "Eager to learn!",
        "location": "Accra"
    },
    "sender_tutor": null,
    "receiver": 2,
    "receiver_student": null,
    "receiver_tutor": {
        "id": 2,
        "profile_picture": null,
        "expertise": "Mathematics, Physics",
        "hourly_rate": "30.00",
        "online_availability": "Monday-Friday Evenings",
        "in_person_availability": "Saturday Mornings",
        "location": "Accra"
    },
    "content": "Hello, are you available tomorrow?",
    "timestamp": "2025-04-06T19:22:00.000Z",
    "is_read": false
}
List Messages (Read - GET)
Endpoint: /api/communications/messages/
Method: GET
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 200 OK): Returns a list of message objects. You'll likely need to implement filtering (e.g., by sender, receiver, or conversation) in your viewset to make this more useful.

Retrieve Message (Read - GET)
Endpoint: /api/communications/messages/{message_id}/ (Replace {message_id} with the actual ID)
Method: GET
Headers: Authorization: Bearer [your_access_token]

Expected Response (Success - HTTP 200 OK): Returns the details of the specific message.

JSON

{
    "id": 1,
    "sender": 1,
    "sender_student": {
        "id": 1,
        "profile_picture": null,
        "bio": "Eager to learn!",
        "location": "Accra"
    },
    "sender_tutor": null,
    "receiver": 2,
    "receiver_student": null,
    "receiver_tutor": {
        "id": 2,
        "profile_picture": null,
        "expertise": "Mathematics, Physics",
        "hourly_rate": "30.00",
        "online_availability": "Monday-Friday Evenings",
        "in_person_availability": "Saturday Mornings",
        "location": "Accra"
    },
    "content": "Hello, are you available tomorrow?",
    "timestamp": "2025-04-06T19:22:00.000Z",
    "is_read": false
}
Update Message (Update - PATCH)
While you might not typically update the content of a sent message, you might want to update the is_read status.

Endpoint: /api/communications/messages/{message_id}/
Method: PATCH
Headers: Content-Type: application/json, Authorization: Bearer [your_access_token]
Body (Raw - JSON - Example):

JSON

{
    "is_read": true
}
Expected Response (Success - HTTP 200 OK): Returns the updated message details.

JSON

{
    "id": 1,
    "sender": 1,
    "sender_student": {
        "id": 1,
        "profile_picture": null,
        "bio": "Eager to learn!",
        "location": "Accra"
    },
    "sender_tutor": null,
    "receiver": 2,
    "receiver_student": null,
    "receiver_tutor": {
        "id": 2,
        "profile_picture": null,
        "expertise": "Mathematics, Physics",
        "hourly_rate": "30.00",
        "online_availability": "Monday-Friday Evenings",
        "in_person_availability": "Saturday Mornings",
        "location": "Accra"
    },
    "content": "Hello, are you available tomorrow?",
    "timestamp": "2025-04-06T19:22:00.000Z",
    "is_read": true
}
Delete Message (Delete - DELETE)
Endpoint: /api/communications/messages/{message_id}/
Method: DELETE
Headers: Authorization: Bearer [your_access_token]
Body: (No request body is typically required for a DELETE operation)

Expected Response (Success - HTTP 204 No Content): An empty response with a 204 No Content status code.
