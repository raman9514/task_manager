from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Task, User
from .serializers import AssignTaskSerializer, UserWithTasksSerializer, CreateTaskSerializer,TaskSerializer

class CreateTaskView(APIView):
    """
    API endpoint to create a new task.

    Example Request:
    ```
    {
        "name": "New Task 4",
        "description": "This is a test task",
        "task_type": "Bug Fix",
        "status": "pending",
        "assigned_users": [1, 2]
    }
    ```

    Example Response:
    ```
    {
        "message": "Task created successfully",
        "task": {
            "id": 1,
            "name": "New Task 4",
            "description": "This is a test task",
            "task_type": "Bug Fix",
            "status": "pending",
            "assigned_users": [1, 2]
        }
    }
    ```
    """
    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task_serializer = TaskSerializer(task) 
            return Response({"message": "Task created successfully", "task": task_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignTaskView(APIView):
    """
    API endpoint to assign a task to users.

    Example Request:
    ```
    {
        "task_id": 1,
        "user_ids" : [1,2]
    }
    ```

    Example Response:
    ```
    {
        "message": "Task assigned successfully",
        "task_id": 1,
        "assigned_users": [1, 2]
    }
    ```
    """
    def post(self, request):
        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            task = get_object_or_404(Task, id=serializer.validated_data['task_id'])
            users = User.objects.filter(id__in=serializer.validated_data['user_ids'])
            task.assigned_users.set(users)
            return Response({
                "message": "Task assigned successfully",
                "task_id": task.id,
                "assigned_users": users
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTasksView(APIView):
    """
    API endpoint to get all tasks assigned to a specific user.

    Example Response:
    ```
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
    """
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserWithTasksSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
