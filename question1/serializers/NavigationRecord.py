from rest_framework import serializers
from ..models import NavigationRecord

class NavigationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields='__all__'

