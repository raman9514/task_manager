# Task Management API - Django & DRF

## Overview
This is a **Task Management API** built using **Django** and **Django REST Framework (DRF)**. It provides endpoints to **create tasks, assign tasks to users, and fetch assigned tasks**. The API follows RESTful best practices and includes **proper validation for required fields**.

## Features
- ✅ Create new tasks with a name, description, and status
- ✅ Assign tasks to one or multiple users
- ✅ Retrieve all tasks assigned to a specific user
- ✅ User creation with email, mobile, and password authentication
- ✅ Well-documented APIs with example requests and responses

## Technologies Used
- **Django** & **Django REST Framework**
- **PostgreSQL** (or SQLite for development)
- **Docker** (if needed for deployment)

## Setup Instructions

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/raman9514/task_manager.git
$ cd task_manager
```

### 2️⃣ Setting Up Without Docker

#### Create and Activate a Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies
```sh
$ pip install -r requirements.txt
```

#### Apply Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create a Superuser (Optional, for Admin Access)
```sh
$ python manage.py createsuperuser
```

#### Run the Server
```sh
$ python manage.py runserver
```

---

### 3️⃣ Setting Up with Docker

#### **Build the Docker Image**
```sh
$ docker build -t task-management-api .
```

#### **Run the Docker Container**
```sh
$ docker run -p 8000:8000 task-management-api
```

#### **Run Migrations in Docker**
```sh
$ docker run task-management-api python manage.py migrate
```

#### **Create a Superuser in Docker**
```sh
$ docker run -it task-management-api python manage.py createsuperuser
```

#### **Stop Running Containers**
```sh
$ docker ps  # Find the container ID
$ docker stop <container_id>
```

---

## API Endpoints & Field Requirements

### **1️⃣ Create a User**
📌 **Endpoint:** `POST /api/users/create/`

**Required Fields:**
- `username` (string) - **Mandatory**
- `email` (string) - **Mandatory** (must be unique)
- `mobile` (string) - **Mandatory**
- `password` (string) - **Mandatory**

**Request Body:**
```json
{
    "username": "john_doe",
    "email": "johndoe@example.com",
    "mobile": "9876543210",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "message": "User created successfully",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "johndoe@example.com",
        "mobile": "9876543210"
    }
}
```

---

### **2️⃣ Create a Task**
📌 **Endpoint:** `POST /api/tasks/create/`

**Required Fields:**
- `name` (string) - **Mandatory**
- `description` (string) - **Mandatory**
- `task_type` (string) - **Mandatory**
- `status` (string) - **Mandatory** (e.g., `pending`, `in_progress`, `completed`)
- `assigned_users` (list of user IDs) - **Optional**

**Request Body:**
```json
{
    "name": "New Task 4",
    "description": "This is a test task",
    "task_type": "Bug Fix",
    "status": "pending",
    "assigned_users": [1]
}
```

**Response:**
```json
{
    "message": "Task created successfully",
    "task": {
        "id": 1,
        "name": "New Task 4",
        "description": "This is a test task",
        "task_type": "Bug Fix",
        "status": "pending",
        "assigned_users": [1]
    }
}
```

---

### **3️⃣ Assign Task to Users**
📌 **Endpoint:** `POST /api/tasks/assign/{task_id}/`

**Required Fields:**
- `assigned_users` (list of user IDs) - **Mandatory**

**Request Body:**
```json
{
    "assigned_users": [1, 2]
}
```

**Response:**
```json
{
    "message": "Task assigned successfully",
    "task_id": 1,
    "assigned_users": [1, 2]
}
```

---

### **4️⃣ Get Tasks Assigned to a Specific User**
📌 **Endpoint:** `GET /api/users/{user_id}/tasks/`

**Response Example:**
```json
{
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com"
    },
    "tasks": [
        {
            "id": 1,
            "name": "Fix UI Bug",
            "description": "Fix the issue with the login button.",
            "task_type": "Bug Fix",
            "status": "pending"
        },
        {
            "id": 2,
            "name": "Optimize DB",
            "description": "Improve database queries.",
            "task_type": "Performance",
            "status": "in_progress"
        }
    ]
}
```

---



