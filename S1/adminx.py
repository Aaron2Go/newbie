from django.contrib import admin
from S1.models import *
#from S2.models import *
import xadmin


class StockLedgeAdmin(object):
    list_display = [
        'InfoDate',
        'Code',
        'Name',
        'Holdings',
        'Project_Nums',
        'Project_Nums_20',
        'Price',
        'MV',
        'Turnover_Rate',
        'Days_to_Settle',
    ]


xadmin.site.register(StockLedge, StockLedgeAdmin)
