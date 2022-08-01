from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='login'),
    path('auth/token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("auth/logout/", views.logout_view, name="logout_view")
    ]