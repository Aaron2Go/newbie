from django.contrib import admin
from S3.models import *


# Register your models here.

@admin.register(PlBranch)
class PlBranchAdmin(admin.ModelAdmin):
    pass

@admin.register(PlProject)
class PlProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(NavFile)
class NavFileAdmin(admin.ModelAdmin):
    # list_display = ('Project', 'InfoDate', 'Filename', 'File', 'FileType', 'UploadedDateTime', 'LastModifiedDateTime', 'ModifiedTimes', 'Comments')
    #list_display = (
    #'Filename', 'File', 'FileType', 'UploadedDateTime', 'LastModifiedDateTime', 'ModifiedTimes', 'Comments')
    pass
