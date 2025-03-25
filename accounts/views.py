from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer

class CreateUserView(APIView):
    """
    API endpoint to create a new user.
    
    Example Request:
    ```
    {
        "username": "john_doe",
        "email": "johndoe@example.com",
        "mobile": "9876543210",
        "password": "securepassword123"
    }
    ```

    Example Response:
    ```
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
    """
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully", "user": serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
