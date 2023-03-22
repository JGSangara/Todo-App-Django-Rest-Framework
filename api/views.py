from rest_framework import generics

from tasks.models import Task
from .serializers import TaskSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "success": True,
            "status code": status.HTTP_200_OK,
            "message": "User logged in  successfully",
            "token": serializer.data['token']
        }, status=status.HTTP_200_OK)
