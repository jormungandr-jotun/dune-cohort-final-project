from django.contrib import admin
from .models import Inquiry, Property, PropertyImage, SavedProperty

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "property_type", "status", "price", "owner", "created_at")
    list_filter = ("status", "property_type", "city")
    search_fields = ("title", "address", "city", "owner__username")
    inlines = [PropertyImageInline]

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("property", "sender", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("property__title", "sender__username")

admin.site.register(SavedProperty)
