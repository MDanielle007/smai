from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = "Seed the database with default users"

    def handle(self, *args, **kwargs):
        users_data = [
            {"name": "Admin User", "email": "admin@example.com", "password": "Admin123!", "role": "admin", "is_staff": True, "is_superuser": True},
            {"name": "Service Provider", "email": "provider@example.com", "password": "Provider123!", "role": "service_provider", "is_staff": False, "is_superuser": False},
            {"name": "End User", "email": "user@example.com", "password": "User123!", "role": "end_user", "is_staff": False, "is_superuser": False},
        ]

        for user_data in users_data:
            email = user_data["email"]
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(
                    email=email,
                    name=user_data["name"],
                    password=user_data["password"],
                    role=user_data["role"],
                    is_staff=user_data["is_staff"],
                    is_superuser=user_data["is_superuser"],
                )
                self.stdout.write(self.style.SUCCESS(f"User {email} created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"User {email} already exists"))
