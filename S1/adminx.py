from django.contrib import admin
from S1.models import *  # Project, Branch, Stock
#from S2.models import *
import xadmin


class ZZpp(object):
    list_display = [
        'Name',
        'stock_num',
        'stock_num_trade',
        'stock_num_sup',
    ]

    def queryset(self):
        qs = super(ZZpp, self).queryset()
        qs = qs.filter(Type='配资类')
        return qs


xadmin.site.register(ZProject, ZZpp)
