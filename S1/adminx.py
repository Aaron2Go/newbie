from django.contrib import admin
from S1.models import *  # Project, Branch, Stock
#from S2.models import *
import xadmin


class StockLedgeAdmin(object):
    pass


xadmin.site.register(StockLedge, StockLedgeAdmin)
