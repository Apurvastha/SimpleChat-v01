# Simple Chat App

A real-time messaging web application built using **Django**. It allows users to register, log in, and send messages to each other.

## 🚀 Features
- User authentication (login & logout)
- Real-time messaging between users
- Messages are stored in a database
- Secure user access with Django's authentication system

## 🛠️ Tech Stack
- **Backend:** Django, Django ORM
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default) or PostgreSQL/MySQL (optional)
- **Authentication:** Django's built-in user model

## 📂 Project Structure
```
SimpleChat/
├── chat/                  # Django app for messaging
│   ├── migrations/        # Database migrations
│   ├── __pycache__/       # Compiled Python files
│   ├── admin.py           # Admin panel configurations
│   ├── apps.py            # Django app configuration
│   ├── models.py          # Defines the Message model
│   ├── tests.py           # Test cases
│   ├── urls.py            # URL routing for the chat app
│   ├── views.py           # Handles message sending and retrieval
│   ├── __init__.py        # App initialization
│
├── SajiloChat/            # Main Django project folder
│   ├── __pycache__/       # Compiled Python files
│   ├── __init__.py        # Project initialization
│   ├── asgi.py            # ASGI application entry point
│   ├── settings.py        # Project settings
│   ├── urls.py            # Global URL routing
│   ├── wsgi.py            # WSGI application entry point
│
├── static/                # Static files (CSS, JS, images)
│
├── templates/chat/        # HTML templates for the chat app
│   ├── base.html          # Common layout template
│   ├── chat_room.html     # Chat interface
│   ├── login.html         # User authentication page
│   ├── user_list.html     # Displays registered users
│
├── venv/                  # Virtual environment (not tracked in Git)
├── .gitignore             # Files to exclude from Git
├── db.sqlite3             # SQLite database file
├── manage.py              # Django project management script
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
```

## 🔧 Installation & Setup
Follow these steps to set up and run the project on your local machine:

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/Apurvastha/SimpleChat-v01
cd SimpleChat
```

### 2️⃣ **Create a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

pip install -r requirements.txt
```

### 3️⃣ **Apply Database Migrations**
```sh
python manage.py migrate
```

### 4️⃣ **Create a Superuser (Admin)**
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 5️⃣ **Run the Development Server**
```sh
python manage.py runserver
```
Open your browser and go to:  
🔗 **http://127.0.0.1:8000/**

## 📌 How It Works
1. Users log in using their credentials.
2. They can see a list of registered users.
3. Clicking on a user opens a chat room where they can send and receive messages in real time.
4. Messages are stored in the database and retrieved upon loading the chat.

## 📌 API Endpoints
| Endpoint            | Method | Description |
|---------------------|--------|-------------|
| `/login/`           | POST   | User login |
| `/logout/`          | GET    | User logout |
| `/user-list/`       | GET    | Get list of users |
| `/chat/<receiver_id>/` | GET | Open chat room with a user |
| `/send-message/`    | POST   | Send a message |
| `/get-messages/<receiver_id>/` | GET | Retrieve messages with a user |

## 🔒 Security Considerations
- User authentication is required to access messages.
- Messages are private and visible only to the sender and receiver.

## 📞 Contact
For any issues or contributions, feel free to submit a pull request or open an issue.

---

Happy coding! 🚀

