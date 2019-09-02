from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializers a name field for testing our api"""

    name = serializers.CharField(max_length=10)
