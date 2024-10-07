from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from film.api import viewsets as filmviewset
from film import views

route = routers.DefaultRouter()

route.register(r'films', filmviewset.FilmViewSet, basename='Films')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('films/', views.FilmAPIView.as_view(), name='films-list-create'),
    path('films/<int:pk>/', views.FilmAPIView.as_view(), name='films-detail-update-delete'),
    path('select/', views.FilmAPIView.home, name='film-list')
]
