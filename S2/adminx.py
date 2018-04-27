from django.contrib import admin
from S2.models import *  # Project, Branch, Stock
import xadmin
from xadmin import views


# https://outin.github.io/newbie/
class GlobalSettings(object):
    site_title = '底仓管理系统'
    site_footer = '2018 李旭 & 赵新宇 '
    # menu_style = 'accordion' 修改侧边栏样式为折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


class BaseSetting(object):
    enable_themes = True  # 表示使用主题功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


# Register your models here.

class BranchAdmin(object):
    list_display = ['Name', 'Area']


xadmin.site.register(Branch, BranchAdmin)


class ProjectAdmin(object):
    data_charts = {
        "user_count": {
            'title': u"User Report",
            "x-field": "Amount",
            "y-field": "Duration",
            "order": (
                'Amount',
            )
        },
    }
    list_display = [
        'ID',
        'Name',
        'Branch',
        'Type',
        'Issue_Date',
        'Duration',
        'Amount',
        'Leverage_Ratio',
    ]
    list_filter = [
        'Branch',
        'Type',
    ]
    search_fields = [
        'ID',
        'Name',
        'Branch__Name',
        'Branch__Area',
        'Type',
    ]


xadmin.site.register(Project, ProjectAdmin)


class GuarantorAdmin(object):
    list_display = [
        'ID',
        'Name',
        'Project',
    ]


xadmin.site.register(Guarantor, GuarantorAdmin)


class AdviserAdmin(object):
    list_display = [
        'ID',
        'Name',
        'Project',
    ]


xadmin.site.register(Adviser, AdviserAdmin)


class PosteriorAdmin(object):
    list_display = [
        'ID',
        'Name',
        'Project',
    ]


xadmin.site.register(Posterior, PosteriorAdmin)


class NavDataAdmin(object):
    list_display = [
        #'Project',
        #'InfoDate',
        'Code',
        'Name',
        'Holdings',
        'Purchase_Price',
        'Costs',
        'Cost_to_NAV',
        'Market_Price',
        'Market_Value',
        'Market_Value_to_NAV',
        'Valuation',
        'Status',
    ]
    search_fields = [
        'Code',
        'Name',
        'Project__Name',
        'Project__ID',
        'Project__Branch__Name',
        'Project__Branch__Area',
        'Project__Type',
    ]
    list_filter = [
        'Status',
        'Project__Branch',
        'InfoDate',
    ]


xadmin.site.register(NavData, NavDataAdmin)
