from django.contrib import admin
from S3.models import *
import xadmin


# Register your models here.


class PlBranchAdmin(object):
    pass


xadmin.site.register(PlBranch, PlBranchAdmin)


class PlProjectAdmin(object):
    pass


xadmin.site.register(PlProject, PlProjectAdmin)


class NavFileAdmin(object):
    # list_display = ('Project', 'InfoDate', 'Filename', 'File', 'FileType', 'UploadedDateTime', 'LastModifiedDateTime', 'ModifiedTimes', 'Comments')
    # list_display = (
    # 'Filename', 'File', 'FileType', 'UploadedDateTime', 'LastModifiedDateTime', 'ModifiedTimes', 'Comments')
    pass


xadmin.site.register(NavFile, NavFileAdmin)
