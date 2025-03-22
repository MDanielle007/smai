from rest_framework import serializers
from bookings.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service.name", read_only=True)
    provider_name = serializers.CharField(source="provider.name", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "user", "user_name", "service", "service_name", "provider", "provider_name", "status", "booked_at", "scheduled_date"]
        read_only_fields = ["status", "user", "provider", "booked_at"]

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["user"] = request.user  # Ensure the logged-in user is the one booking
        return super().create(validated_data)
