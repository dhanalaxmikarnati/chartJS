
from rest_framework import serializers
from .models import Dashboard

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'  # Use '__all__' to include all fields from the model
