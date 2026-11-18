import django.core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name="Property", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=180)),
            ("description", models.TextField()),
            ("property_type", models.CharField(choices=[("apartment", "Apartment"), ("house", "House"), ("land", "Land"), ("commercial", "Commercial")], default="apartment", max_length=20)),
            ("status", models.CharField(choices=[("available", "Available"), ("rented", "Rented"), ("sold", "Sold")], default="available", max_length=20)),
            ("price", models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0)])),
            ("address", models.CharField(max_length=255)), ("city", models.CharField(max_length=100)),
            ("bedrooms", models.PositiveSmallIntegerField(default=0)), ("bathrooms", models.PositiveSmallIntegerField(default=0)),
            ("area_sq_m", models.PositiveIntegerField(default=0, help_text="Floor area in square metres")),
            ("cover_image", models.ImageField(blank=True, null=True, upload_to="property_covers/")),
            ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)),
            ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="properties", to=settings.AUTH_USER_MODEL)),
        ], options={"ordering": ["-created_at"]}),
        migrations.CreateModel(name="Inquiry", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("message", models.TextField()), ("created_at", models.DateTimeField(auto_now_add=True)), ("is_read", models.BooleanField(default=False)),
            ("property", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="inquiries", to="listings.property")),
            ("sender", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="inquiries", to=settings.AUTH_USER_MODEL)),
        ]),
        migrations.CreateModel(name="PropertyImage", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("image", models.ImageField(upload_to="property_gallery/")), ("caption", models.CharField(blank=True, max_length=150)),
            ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ("property", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="images", to="listings.property")),
        ]),
        migrations.CreateModel(name="SavedProperty", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("saved_at", models.DateTimeField(auto_now_add=True)),
            ("property", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="saved_by", to="listings.property")),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="saved_properties", to=settings.AUTH_USER_MODEL)),
        ], options={"unique_together": {("user", "property")}}),
    ]
