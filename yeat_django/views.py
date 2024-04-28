from rest_framework import generics

from yeat_django.models import Guild
from yeat_django.serializers import GuildsSerializer

class GuildList(generics.ListCreateAPIView):
    queryset = Guild.objects.all()
    serializer_class = GuildsSerializer

class GuildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guild.objects.all()
    serializer_class = GuildsSerializer
