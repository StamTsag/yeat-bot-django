from rest_framework import serializers
from .models import Guild

class GuildsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ['guildId', 'logging', 'prompts', 'automated', 'automation_channel', 'mention_only']
        extra_kwargs = {'guildId': {'required': True}}
