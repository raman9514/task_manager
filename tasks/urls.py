from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView

urlpatterns = [
    path('create/', CreateTaskView.as_view(), name='create-task'),
    path('assign/', AssignTaskView.as_view(), name='assign-task'),
    path('user/<int:user_id>/', UserTasksView.as_view(), name='user-tasks'),
]
