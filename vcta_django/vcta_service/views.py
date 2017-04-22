from rest_framework import generics, filters

from . import models
from . import serializers


class HeroList(generics.ListCreateAPIView):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer


class HeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer


class TripList(generics.ListCreateAPIView):
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('date',)
    ordering = ('-date',)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer


class TeamList(generics.ListCreateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
