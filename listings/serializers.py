from rest_framework import serializers
from .models import Property, Inquiry

class PropertySerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Property
        fields = ["id", "owner_username", "title", "description", "property_type", "status",
                  "price", "address", "city", "bedrooms", "bathrooms", "area_sq_m",
                  "cover_image", "created_at"]
        read_only_fields = ["id", "owner_username", "created_at"]

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ["id", "property", "sender", "message", "created_at", "is_read"]
        read_only_fields = ["id", "sender", "created_at", "is_read"]
