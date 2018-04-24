from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .readxlsx import *


@receiver(post_save , sender = NavFile)
def import_to_navdata(sender, instance, **kwargs):
    interpret_stock(NavFile.objects.values('File').order_by('UploadedDateTime').last()['File'])

@receiver(post_save , sender = PlBranch)
def import_to_branch(sender, instance, **kwargs):
    interpret_branch(PlBranch.objects.values('File').order_by('UploadedDateTime').last()['File'])