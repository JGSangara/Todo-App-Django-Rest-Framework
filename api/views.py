from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from accounts.models import User
from tasks.models import Task

from .serializers import (
    ChangePasswordSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    TaskSerializer,
    UserSerializer,
)

# Create your views here.


class TaskList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Authentication


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "status code": status.HTTP_201_CREATED,
                "message": "User registered  successfully",
            },
            status=status.HTTP_201_CREATED,
        )


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        user = User.objects.filter(Q(email=email)).first()
        if user:
            token = default_token_generator.make_token(user)
            reset_url = request.build_absolute_uri(
                reverse(
                    "api:password_reset_confirm",
                    kwargs={"uidb64": user.pk, "token": token},
                )
            )
            send_mail(
                subject="Password Reset",
                message=f"Click this link to reset your password: {reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

        return Response(
            {
                "message": "Please check your email for instructions on how to reset your password."
            },
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")

        try:
            uid = int(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response(
                {"message": "Your password has been reset."}, status=status.HTTP_200_OK
            )

        return Response(
            {"message": "Invalid reset link."}, status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(
            {
                "success": True,
                "status code": status.HTTP_200_OK,
                "message": "User logged out successfully",
            },
            status=status.HTTP_200_OK,
        )
