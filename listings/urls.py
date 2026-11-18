from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("properties/", views.property_list, name="property_list"),
    path("properties/<int:pk>/", views.property_detail, name="property_detail"),
    path("properties/add/", views.property_create, name="property_create"),
    path("properties/<int:pk>/edit/", views.property_update, name="property_update"),
    path("properties/<int:pk>/delete/", views.property_delete, name="property_delete"),
    path("properties/<int:pk>/save/", views.save_property, name="save_property"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("staff/inquiries/", views.staff_inquiries, name="staff_inquiries"),
]
