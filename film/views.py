from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .api.serializers import FilmSerializer
from rest_framework import status
from .models import Films


class FilmAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            film = Films.objects.get(pk=pk)
            serializer = FilmSerializer(film)
        else:
            films = Films.objects.all()
            serializer = FilmSerializer(films, many=True)
        return Response(serializer.data, status=status.HTTP_200_ok)
    
    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        film = Films.objects.get(pk=pk)
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        film = Films.objects.get(pk=pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @api_view(['GET'])
    def home(request):
        if request.method == 'GET':
            category = request.GET.get('category', None)
            if category:
                films = Films.objects.filter(category__icontains=category)
            else:
                films = Films.objects.all()

            serializer = FilmSerializer(films, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    