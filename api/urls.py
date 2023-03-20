from django.urls import path
from .views import TaskList, TaskDetail

app_name = 'api'

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
