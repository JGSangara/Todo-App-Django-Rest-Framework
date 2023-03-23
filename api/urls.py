from django.urls import path
from .views import TaskList, TaskDetail, LoginView, RegisterView

app_name = 'api'

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    # authentication
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/register/', RegisterView.as_view(), name='register'),

]
