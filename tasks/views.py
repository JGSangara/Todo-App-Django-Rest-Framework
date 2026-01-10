from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskListCreateAPIView (generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
