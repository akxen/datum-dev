from rest_framework import serializers

from .models import DispatchSCADA, DispatchReportCaseSolution


class DispatchSCADASerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchSCADA
        fields = ['settlementdate', 'duid', 'scadavalue']


class DispatchReportCaseSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchReportCaseSolution
        exclude = ['row_id']
