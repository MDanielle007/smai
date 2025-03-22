from django.urls import path
from .views import LoginView, LogoutView, RefreshTokenView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("api/token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]