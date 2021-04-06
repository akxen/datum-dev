from rest_framework import serializers

from .models import DispatchSCADA


class DispatchSCADASerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchSCADA
        fields = ['settlementdate', 'duid', 'scadavalue']
