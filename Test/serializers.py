from rest_framework_mongoengine import serializers
from Test.models import Driver

class DriverSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Driver
        fields = '__all__'