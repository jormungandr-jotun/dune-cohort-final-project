from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

class Property(models.Model):
    PROPERTY_TYPES = [
        ("apartment", "Apartment"), ("house", "House"), ("land", "Land"),
        ("commercial", "Commercial"),
    ]
    STATUS_CHOICES = [("available", "Available"), ("rented", "Rented"), ("sold", "Sold")]
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=180)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default="apartment")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    price = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(0)])
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    bedrooms = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    area_sq_m = models.PositiveIntegerField(default=0, help_text="Floor area in square metres")
    cover_image = models.ImageField(upload_to="property_covers/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.city}"

    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"pk": self.pk})

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="property_gallery/")
    caption = models.CharField(max_length=150, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Image for {self.property.title}"

class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inquiries")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inquiries")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Inquiry by {self.sender} about {self.property}"

class SavedProperty(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="saved_properties")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "property")

    def __str__(self):
        return f"{self.user} saved {self.property}"
