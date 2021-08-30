from datetime import datetime, timedelta
from rest_framework.response import Response
from django.db.models import Max
from rest_framework.views import APIView
from .models import NavigationRecord


class NavigationRecordAPI(APIView):
    def get(self,request):
        time_ = datetime.now() - timedelta(hours=48)
        records = NavigationRecord.objects.filter(datetime__gte=time_).values('latitude','longitude','vehicle__plate')\
            .annotate(datetime = Max('datetime'))

        return Response({"last_points":records})