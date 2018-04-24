from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from S3.post_save_action import *



