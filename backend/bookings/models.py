from django.db import models
from users.models import User
from services.models import Service

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")  # End-user
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="bookings")
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="provider_bookings")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booked_at = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateField()

    def __str__(self):
        return f"{self.user.name} booked {self.service.name} ({self.get_status_display()})"
