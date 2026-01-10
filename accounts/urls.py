from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    ChangePasswordView,
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetView,
    RegisterView,
    UserDetailView,
)

app_name = "accounts"

urlpatterns = [
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", RegisterView.as_view(), name="register"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
