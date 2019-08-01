from first_app import models
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Music
        fields=['title','artist','genre','track_no']