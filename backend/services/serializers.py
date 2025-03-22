from rest_framework import serializers
from services.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source="provider.name", read_only=True)

    class Meta:
        model = Service
        fields = ["id", "name", "description", "price", "status", "provider", "provider_name", "created_at"]
        read_only_fields = ["status", "provider", "created_at"]  # Prevent unauthorized edits

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["provider"] = request.user  # Ensure only the logged-in provider can create services
        return super().create(validated_data)

