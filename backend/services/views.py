from rest_framework import viewsets, permissions
from services.models import Service
from services.serializers import ServiceSerializer
from users.permissions import IsAdmin, IsServiceProvider
from rest_framework.decorators import action
from rest_framework.response import Response

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        """ Restrict data based on user role """
        user = self.request.user

        if user.role == "admin":
            return Service.objects.all()  # Admin sees all services
        elif user.role == "service_provider":
            return Service.objects.filter(provider=user)  # Providers see only their services
        else:
            return Service.objects.filter(status="approved")  # End-users see only approved services

    def get_permissions(self):
        """ Assign permissions based on action """
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsServiceProvider]  # Providers manage their own services
        elif self.action in ["approve", "reject"]:
            permission_classes = [IsAdmin]  # Only admins can approve/reject
        else:
            permission_classes = [permissions.AllowAny]  # Anyone can view approved services
        return [perm() for perm in permission_classes]

    @action(detail=True, methods=["post"], permission_classes=[IsAdmin])
    def approve(self, request, pk=None):
        """ Admin can approve a service """
        service = self.get_object()
        service.status = "approved"
        service.save()
        return Response({"message": "Service approved successfully"})

    @action(detail=True, methods=["post"], permission_classes=[IsAdmin])
    def reject(self, request, pk=None):
        """ Admin can reject a service """
        service = self.get_object()
        service.status = "rejected"
        service.save()
        return Response({"message": "Service rejected"})
