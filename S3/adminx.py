from django.contrib import admin
from S3.models import *
import xadmin


# Register your models here.


class BranchFileAdmin(object):
    list_display = [
        'File',
        'UploadTime',
        'Comments',
    ]
    search_fields = [
        'File',
        'Comments',
    ]


xadmin.site.register(BranchFile, BranchFileAdmin)


class ProjectFileAdmin(object):
    list_display = [
        'File',
        'UploadTime',
        'Comments',
    ]
    search_fields = [
        'File',
        'Comments',
    ]


xadmin.site.register(ProjectFile, ProjectFileAdmin)


class NavFileAdmin(object):
    list_display = [
        'Project',
        'File',
        'UploadTime',
        'Comments',
    ]
    search_fields = [
        'Project',
        'Comments',
    ]


xadmin.site.register(NavFile, NavFileAdmin)
