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


class P5MinCaseSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5MinCaseSolution
        exclude = ['row_id']


class P5MinRegionSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5MinRegionSolution
        exclude = ['row_id']


class P5MinInterconnectorSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5MinInterconnectorSolution
        exclude = ['row_id']


class P5MinConstraintSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.P5MinConstraintSolution
        exclude = ['row_id']
