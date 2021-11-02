from rest_framework import serializers
from location.models import User_location


class User_locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_location
        fields = "__all__"
