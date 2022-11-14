from rest_framework import serializers


class BlogSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=10)
