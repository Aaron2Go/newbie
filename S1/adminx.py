from django.contrib import admin
from S1.models import *
# from S2.models import *
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


class ProjectLedgeAdmin(object):
    list_display = [
        'InfoDate',
        'Project',
        'Branch',
        'Type',
        'Approval_Form_Num',
        'Issue_Date',
        'Duration',
        'Amount',
        'Leverage_Ratio',
        'Stock_Num',
        'Stock_Num_ST',
        'Stock_Num_Suspend',
        'First_Record_Date',
        'Current_Nav',
        'Nav_Warn',
        'Nav_Stop',
    ]


xadmin.site.register(ProjectLedge, ProjectLedgeAdmin)


class BranchLedgeAdmin(object):
    list_display = [
        'InfoDate',
        'Branch',
        'Amounts_Total',
        'Amounts_Avg',
        'Project_Num',
        'Project_Num_ST',
        'Project_Num_Suspend',
        'Project_Num_Normal',
        'Project_Num_Warn',
        'Project_Num_Stop',
        'Stock_Num',
        'Stock_Num_Suspend',
        'Stock_Num_ST',
        'Days_Settle_Max',
        'Days_Settle_Avg',
        'Days_Settle_Mid',
    ]


xadmin.site.register(BranchLedge, BranchLedgeAdmin)
