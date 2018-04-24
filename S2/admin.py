from django.contrib import admin
from S2.models import *  # Project, Branch, Stock

admin.site.site_header = '底仓监控系统'
admin.site.site_title = '底仓监控系统'


# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Area')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'Branch', 'Type', 'Approval_Form_Num', 'Issue_Date', 'Duration', 'Amount',
                    'Leverage_Ratio')
    fk_fields = ('Name',)


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
    # list_display = ('Project', 'InfoDate', 'Code', 'Name', 'Holdings', 'Purchase_Price', 'Costs', 'Cost_to_NAV', 'Market_Price', 'Market_Value', 'Market_Value_to_NAV', 'Valuation', 'Status')
    list_display = ('Code', 'Name', 'Holdings', 'Purchase_Price', 'Costs', 'Cost_to_NAV', 'Market_Price', 'Market_Value', 'Market_Value_to_NAV', 'Valuation', 'Status')


