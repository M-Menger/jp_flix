from rest_framework import viewsets
from film.api import serializers
from film import models

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmSerializer
    queryset = models.Films.objects.all()
    