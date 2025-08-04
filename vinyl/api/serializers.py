from rest_framework import serializers

class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    year = serializers.IntegerField(required=False, allow_null=True)
    genre = serializers.CharField(max_length=100, required=False, allow_null=True)
