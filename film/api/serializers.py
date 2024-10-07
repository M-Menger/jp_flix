from rest_framework import serializers
from film import models

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Films
        fields = '__all__'
        