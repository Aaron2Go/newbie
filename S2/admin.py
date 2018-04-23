from django.contrib import admin
from S2.models import *  # Project, Branch, Stock, TargetFields, ExcelFiles

admin.site.site_header = 'Newbie 数据管理系统'
admin.site.site_title = 'Newbie'


# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Area')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Branch', 'Type', 'Approval_Form_Num', 'Issue_Date', 'Duration', 'Amount',
                    'Leverage_Ratio')
    fk_fields = ('Name',)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('Code', 'Name', 'Holdings', 'Market_Price', 'Market_Value', 'Purchase_Price',
                    'Costs', 'Cost_to_NAV', 'Status')


@admin.register(Guarantor)
class GuarantorAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Project')


@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Project')


@admin.register(Posterior)
class PosteriorAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Project')


@admin.register(NavData)
class NavDataAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Holdings', 'Purchase_Price', 'Costs', 'Cost_to_NAV', 'Market_Value', 'Market_Price', 'Market_Value_to_NAV', 'Valuation', 'Status')


@admin.register(NavFile)
class NavFileAdmin(admin.ModelAdmin):
    list_display = ('Filename', 'File', 'FileType', 'UploadedDateTime', 'LastModifiedDateTime', 'ModifiedTimes', 'Project')