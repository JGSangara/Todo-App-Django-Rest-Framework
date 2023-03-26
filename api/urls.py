from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import ChangePasswordView, RegisterView, TaskDetail, TaskList

app_name = 'api'

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    # authentication
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/login/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/change-password/', ChangePasswordView.as_view(), name='change-password'),

]
