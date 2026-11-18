from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from .serializers import PropertySerializer

class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.select_related("owner").all()
    serializer_class = PropertySerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated()] if self.request.method == "POST" else [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.select_related("owner").all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]

class PropertyDeleteAPIView(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(owner=self.request.user)

class PropertyUpdateAPIView(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset if self.request.user.is_staff else queryset.filter(owner=self.request.user)
