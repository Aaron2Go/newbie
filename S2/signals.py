from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .readxlsx import *


@receiver(post_save , sender = NavFile)
def import_to_navdata(sender, instance, **kwargs):
    handle_excel_data(NavFile.objects.values('File').order_by('UploadedDateTime').last()['File'])
