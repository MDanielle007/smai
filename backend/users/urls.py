from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, LogoutView, RefreshTokenView, RegisterView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("api/token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),
     path("", include(router.urls)),
]