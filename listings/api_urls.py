from django.urls import path
from .api_views import PropertyDeleteAPIView, PropertyDetailAPIView, PropertyListCreateAPIView, PropertyUpdateAPIView

urlpatterns = [
    path("properties/", PropertyListCreateAPIView.as_view(), name="api_property_list_create"),
    path("properties/<int:pk>/", PropertyDetailAPIView.as_view(), name="api_property_detail"),
    path("properties/<int:pk>/update/", PropertyUpdateAPIView.as_view(), name="api_property_update"),
    path("properties/<int:pk>/delete/", PropertyDeleteAPIView.as_view(), name="api_property_delete"),
]
