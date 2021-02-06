"""Result serializer class."""

from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    """Serializer class for the result object."""

    maximum = serializers.FloatField()
    minimum = serializers.FloatField()
    average = serializers.FloatField()
    median = serializers.FloatField()
