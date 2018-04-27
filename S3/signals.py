from django.db.models.signals import post_save
from django.dispatch import receiver
from S3.models import *
from S3.post_save_action import *


@receiver(post_save, sender=PlBranch)
def import_to_branch(sender, instance, **kwargs):
    interpret_branch(PlBranch.objects.values('File').order_by('UploadTime').last()['File'])


@receiver(post_save, sender=NavFile)
def import_to_navdata(sender, instance, **kwargs):
    interpret_stock(
        NavFile.objects.values('File').order_by('UploadTime').last()['File'],
        NavFile.objects.values('Project__ID').order_by('UploadTime').last()['Project__ID'],
        NavFile.objects.values('InfoDate').order_by('UploadTime').last()['InfoDate'],
    )


@receiver(post_save, sender=PlProject)
def import_to_project(sender, instance, **kwargs):
    interpret_project(PlProject.objects.values('File').order_by('UploadTime').last()['File'])
