from django.db.models import Max

from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class DispatchSCADAView(APIView):
    """Dispatch SCADA data snapshot - latest data for all units"""

    def get(self, request, format=None):
        """Get snapshot of latest dispatch for all DUIDs"""

        # Get latest timestamp
        latest_timestamp = models.DispatchSCADA.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = models.DispatchSCADA.objects.filter(settlementdate=timestamp_str)
        serializer = serializers.DispatchSCADASerializer(data, many=True)

        return Response(serializer.data)


class DispatchSCADADetailView(APIView):
    """Dispatch SCADA data view"""

    def get(self, request, format=None):
        """Get data for given DUIDs"""

        # Extract DUIDs
        symbols = request.query_params.get('duid')
        if symbols is None:
            return Response({"message": "Must specify DUID(s)"})
        duids = symbols.split(',')

        # Number of records to extract from database
        n_duids = len(duids)
        observations = 12 * 12

        # TODO: fix this query. Should use group by.
        data = (models.DispatchSCADA.objects.filter(duid__in=duids)
                .order_by('-settlementdate')[:observations * n_duids][::-1])
        serializer = serializers.DispatchSCADASerializer(data, many=True)

        return Response(serializer.data)


class DispatchReportCaseSolutionView(APIView):
    """Latest dispatch report case solution"""

    def get(self, request, format=None):
        """Get snapshot of latest case solution"""

        model = models.DispatchReportCaseSolution
        model_serializer = serializers.DispatchReportCaseSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(settlementdate=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class DispatchReportRegionSolutionView(APIView):
    """Latest dispatch report region solution"""

    def get(self, request, format=None):
        """Get snapshot of latest region solution"""

        model = models.DispatchReportRegionSolution
        model_serializer = serializers.DispatchReportRegionSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(settlementdate=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class DispatchReportInterconnectorSolutionView(APIView):
    """Latest dispatch report interconnector solution"""

    def get(self, request, format=None):
        """Get snapshot of latest interconnector solution"""

        model = models.DispatchReportInterconnectorSolution
        model_serializer = serializers.DispatchReportInterconnectorSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(settlementdate=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class DispatchReportConstraintSolutionView(APIView):
    """Latest dispatch report constraint solution"""

    def get(self, request, format=None):
        """Get snapshot of latest constraint solution"""

        model = models.DispatchReportConstraintSolution
        model_serializer = serializers.DispatchReportConstraintSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(settlementdate=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class P5CaseSolutionView(APIView):
    """Latest P5min report case solution"""

    def get(self, request, format=None):
        """Get snapshot of latest P5min case solution"""

        model = models.P5CaseSolution
        model_serializer = serializers.P5CaseSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('run_datetime'))
        timestamp_str = str(latest_timestamp['run_datetime__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(run_datetime=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class P5RegionSolutionView(APIView):
    """Latest P5min report region solution"""

    def get(self, request, format=None):
        """Get snapshot of latest P5min region solution"""

        model = models.P5RegionSolution
        model_serializer = serializers.P5RegionSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('run_datetime'))
        timestamp_str = str(latest_timestamp['run_datetime__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(run_datetime=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class P5InterconnectorSolutionView(APIView):
    """Latest P5min report interconnector solution"""

    def get(self, request, format=None):
        """Get snapshot of latest P5min interconnector solution"""

        model = models.P5InterconnectorSolution
        model_serializer = serializers.P5InterconnectorSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('run_datetime'))
        timestamp_str = str(latest_timestamp['run_datetime__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(run_datetime=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)


class P5ConstraintSolutionView(APIView):
    """Latest P5min report constraint solution"""

    def get(self, request, format=None):
        """Get snapshot of latest P5min constraint solution"""

        model = models.P5ConstraintSolution
        model_serializer = serializers.P5ConstraintSolutionSerializer

        # Get latest timestamp
        latest_timestamp = model.objects.all().aggregate(Max('run_datetime'))
        timestamp_str = str(latest_timestamp['run_datetime__max'])

        # Extract records corresponding to latest timestamp
        data = model.objects.filter(run_datetime=timestamp_str)
        serializer = model_serializer(data, many=True)

        return Response(serializer.data)
