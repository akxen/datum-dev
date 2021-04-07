from rest_framework import serializers

from . import models


class DispatchSCADASerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DispatchSCADA
        fields = ['settlementdate', 'duid', 'scadavalue']


class DispatchReportCaseSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DispatchReportCaseSolution
        exclude = ['row_id']


class DispatchReportRegionSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DispatchReportRegionSolution
        exclude = ['row_id']


class DispatchReportInterconnectorSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DispatchReportInterconnectorSolution
        exclude = ['row_id']
