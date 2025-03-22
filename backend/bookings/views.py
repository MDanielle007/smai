from rest_framework import viewsets, permissions
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from users.permissions import IsAdmin, IsServiceProvider, IsEndUser
from rest_framework.decorators import action
from rest_framework.response import Response

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer

    def get_queryset(self):
        """ Restrict data based on user role """
        user = self.request.user

        if user.role == "admin":
            return Booking.objects.all()  # Admin sees all bookings
        elif user.role == "service_provider":
            return Booking.objects.filter(provider=user)  # Providers see only their bookings
        else:
            return Booking.objects.filter(user=user)  # End-users see their own bookings

    def get_permissions(self):
        """ Assign permissions based on action """
        if self.action in ["create"]:
            permission_classes = [IsEndUser]  # Only end-users can book services
        elif self.action in ["update", "partial_update", "cancel", "complete"]:
            permission_classes = [IsServiceProvider]  # Providers manage booking statuses
        else:
            permission_classes = [permissions.IsAuthenticated]  # Anyone logged in can view
        return [perm() for perm in permission_classes]

    @action(detail=True, methods=["post"], permission_classes=[IsServiceProvider])
    def confirm(self, request, pk=None):
        """ Service provider confirms a booking """
        booking = self.get_object()
        booking.status = "confirmed"
        booking.save()
        return Response({"message": "Booking confirmed"})

    @action(detail=True, methods=["post"], permission_classes=[IsServiceProvider])
    def complete(self, request, pk=None):
        """ Service provider marks a booking as completed """
        booking = self.get_object()
        booking.status = "completed"
        booking.save()
        return Response({"message": "Booking marked as completed"})

    @action(detail=True, methods=["post"], permission_classes=[IsEndUser])
    def cancel(self, request, pk=None):
        """ End-user cancels their booking """
        booking = self.get_object()
        booking.status = "canceled"
        booking.save()
        return Response({"message": "Booking canceled"})
