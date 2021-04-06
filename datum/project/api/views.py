from django.db.models import Max

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import DispatchSCADA, DispatchReportCaseSolution
from .serializers import DispatchSCADASerializer, DispatchReportCaseSolutionSerializer


class DispatchSCADAView(APIView):
    """Dispatch SCADA data snapshot - latest data for all units"""

    def get(self, request, format=None):
        """Get snapshot of latest dispatch for all DUIDs"""

        # Get latest timestamp
        latest_timestamp = DispatchSCADA.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = DispatchSCADA.objects.filter(settlementdate=timestamp_str)
        serializer = DispatchSCADASerializer(data, many=True)

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
        data = (DispatchSCADA.objects.filter(duid__in=duids)
                .order_by('-settlementdate')[:observations * n_duids][::-1])
        serializer = DispatchSCADASerializer(data, many=True)

        return Response(serializer.data)


class DispatchReportCaseSolutionView(APIView):
    """Latest dispatch report case solution"""

    def get(self, request, format=None):
        """Get snapshot of latest dispatch for all DUIDs"""

        # Get latest timestamp
        latest_timestamp = DispatchReportCaseSolution.objects.all().aggregate(Max('settlementdate'))
        timestamp_str = str(latest_timestamp['settlementdate__max'])

        # Extract records corresponding to latest timestamp
        data = DispatchReportCaseSolution.objects.filter(settlementdate=timestamp_str)
        serializer = DispatchReportCaseSolutionSerializer(data, many=True)

        return Response(serializer.data)
