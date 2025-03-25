from rest_framework import serializers
from .models import Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'      

class CreateTaskSerializer(serializers.ModelSerializer): 
    assigned_users = serializers.ListField(
        child=serializers.IntegerField(), required=False,  # Accept list of user IDs
    )
    class Meta:
        model = Task
        exclude = ['created_at'] 

    def create(self, validated_data):
        assigned_users_data = validated_data.pop('assigned_users', [])  # Get user IDs
        task = Task.objects.create(**validated_data)  # Create the task

        if assigned_users_data:
            users = User.objects.filter(id__in=assigned_users_data)  # Fetch User instances
            task.assigned_users.set(users)  

        return task
    
    
class TaskSerializerHepler(serializers.ModelSerializer): # Helper Serializer For UserWithTaskSerializer
    class Meta:
        model = Task
        exclude = ['assigned_users']  # Excludes assigned_users field

class UserWithTasksSerializer(serializers.ModelSerializer):
    tasks = TaskSerializerHepler(source='tasks.all', many=True)  # Fetch related tasks
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tasks']


class AssignTaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    user_ids = serializers.ListField(child=serializers.IntegerField())
