from rest_framework.serializers import ModelSerializer

from ..models import WorkingHours


class WorkingHoursSerializer(ModelSerializer):

    class Meta:
        model = WorkingHours
        fields = ["day", "start_time", "end_time", "lunch_start_time", "lunch_end_time"]
