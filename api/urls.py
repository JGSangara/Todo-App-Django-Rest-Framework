from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import (ChangePasswordView, LogoutView, PasswordResetConfirmView,
                    PasswordResetView, RegisterView, TaskDetail, TaskList,
                    UserDetailView)

app_name = "api"

urlpatterns = [
    path("tasks/", TaskList.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    # authentication
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("users/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/login/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("users/register/", RegisterView.as_view(), name="register"),
    path(
        "users/change-password/", ChangePasswordView.as_view(), name="change-password"
    ),
    path("users/password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "users/password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("users/logout/", LogoutView.as_view(), name="logout"),
]
