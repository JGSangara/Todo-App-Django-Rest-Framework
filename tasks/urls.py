from django.urls import path

from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

app_name = "tasks"

urlpatterns = [
    path("", TaskListCreateAPIView .as_view(), name="task_list"),
    path("<int:pk>/", TaskRetrieveUpdateDestroyAPIView .as_view(), name="task_detail"),
]
