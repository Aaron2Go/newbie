from django.db.models.signals import post_save
from django.dispatch import receiver
from S3.models import *
from S3.post_save_action import *


@receiver(post_save, sender=BranchFile)
def branchfile_receiver(sender, instance, **kwargs):
    interpret_branchfile(BranchFile.objects.values('File').order_by('UploadTime').last()['File'])


@receiver(post_save, sender=NavFile)
def navfile_receiver(sender, instance, **kwargs):
    interpret_navfile(
        NavFile.objects.values('File').order_by('UploadTime').last()['File'],
        NavFile.objects.values('Project__ID').order_by('UploadTime').last()['Project__ID'],
        NavFile.objects.values('InfoDate').order_by('UploadTime').last()['InfoDate'],
    )


@receiver(post_save, sender=ProjectFile)
def projectfile_receiver(sender, instance, **kwargs):
    interpret_projectfile(ProjectFile.objects.values('File').order_by('UploadTime').last()['File'])
