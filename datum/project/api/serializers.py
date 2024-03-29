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


class DispatchReportConstraintSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DispatchReportConstraintSolution
        exclude = ['row_id']


class P5CaseSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5CaseSolution
        exclude = ['row_id']


class P5RegionSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5RegionSolution
        exclude = ['row_id']


class P5InterconnectorSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5InterconnectorSolution
        exclude = ['row_id']


class P5ConstraintSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5ConstraintSolution
        exclude = ['row_id']
