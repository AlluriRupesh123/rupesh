from rest_framework import serializers
from rupesh.models import rupi
class rupiSerializer(serializers.ModelSerializer):
    class Meta:
        model = rupi
        fields = ('id','name','tz','start_time','end_time','start_times','end_times')

