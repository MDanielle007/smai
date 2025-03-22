from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"

class IsServiceProvider(permissions.BasePermission):
    """
    Allows access only to service providers.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "service_provider"

class IsEndUser(permissions.BasePermission):
    """
    Allows access only to end users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "end_user"
