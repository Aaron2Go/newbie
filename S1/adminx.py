from django.contrib import admin
from S2.models import NavData  # Project, Branch, Stock
import xadmin


class NavData2(NavData):  # 继承 父类 course
    class Meta:
        verbose_name = '底仓查询'
        verbose_name_plural = verbose_name
        proxy = True  # 不会生成新的表

# Register your models here.
#class QueryAdmin(admin.ModelAdmin):
#    def s
class NavDataAdmin2(object):
    list_display = [
        #'Project__Branch__Name',
        #'Project__Name',
        'Project',
        'InfoDate',
        'Code',
        'Name',
        'Holdings',
        'Market_Price',
        'Market_Value',
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

xadmin.site.register(NavData2, NavDataAdmin2)