from django.db import models
from django.core.validators import RegexValidator

class IdValidator(RegexValidator):
    regex = r'^[0-9]+$'
    message = 'Invalid ID.'

class Guild(models.Model):
    guildId             = models.CharField(primary_key=True, unique=True, error_messages={'unique': 'Guild already registered.'}, max_length=20, blank=False, null=False, validators=[IdValidator()])
    logging             = models.BooleanField(default=False)
    prompts             = models.TextField(default='')
    automated           = models.BooleanField(default=False)
    automation_channel  = models.TextField(blank=True, validators=[IdValidator()])
    mention_only        = models.BooleanField(default=False)
