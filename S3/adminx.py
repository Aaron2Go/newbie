from django.contrib import admin
from S3.models import *
import xadmin


# Register your models here.


class PlBranchAdmin(object):
    list_display = [
        'File',
        'UploadTime',
        'Comments',
    ]
    search_fields = [
        'File',
        'Comments',
    ]


xadmin.site.register(PlBranch, PlBranchAdmin)


class PlProjectAdmin(object):
    list_display = [
        'File',
        'UploadTime',
        'Comments',
    ]
    search_fields = [
        'File',
        'Comments',
    ]


xadmin.site.register(PlProject, PlProjectAdmin)


class NavFileAdmin(object):
    list_display = [
        'InfoDate',
        'Project',
        'File',
        'UploadTime',
        'Comments',
    ]
    search_fields = [
        'Project',
        'Comments',
    ]
    list_filter = [
        'InfoDate',
    ]


xadmin.site.register(NavFile, NavFileAdmin)
