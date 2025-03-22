from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from users.models import User

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({error: "Invalid credentials", sucess: False}, status=401)

        login(request, user)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        response = Response({"message": "Login successful", "success": True})
        # For development environment, don't use secure cookies
        response.set_cookie(
            "access_token", 
            str(refresh.access_token), 
            httponly=True, 
            samesite="Lax",
            secure=False,  # Set to False for development
            path="/"    
        )
        response.set_cookie(
            "refresh_token", 
            str(refresh), 
            httponly=True, 
            samesite="Lax",
            secure=False,  # Set to False for development
            path="/"
        )
        
        return response


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    permission_classes = [AllowAny]  # Add this to allow unauthenticated logout
    
    def post(self, request):
        logout(request)
        response = Response({"message": "Logged out successfully"})
        # Add explicit domain and sameSite for cookie deletion
        response.delete_cookie("access_token", path="/", domain=None, samesite="Lax")
        response.delete_cookie("refresh_token", path="/", domain=None, samesite="Lax")
        response.delete_cookie("csrftoken", path="/")
        response.delete_cookie("sessionid", path="/")
        return response


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token missing"}, status=401)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            response = Response({"access_token": str(access_token)})
            response.set_cookie("access_token", str(access_token), httponly=True, samesite="Lax")
            return response
        except Exception:
            return Response({"error": "Invalid refresh token"}, status=401)
