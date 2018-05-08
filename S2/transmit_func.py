from S2.models import StockJournal
from S1.models import StockLedge
from django.utils.timezone import now
import tushare as tu

def generate_stockledge(infodate):
    StockLedge.objects.filter(InfoDate=infodate).delete()
    item_list = StockJournal.objects.filter(InfoDate=infodate).distinct().values('Code')
    for i in item_list:
        records = StockJournal.objects.filter(InfoDate=infodate, Code=i['Code'])

        holdings = 0
        name = "test"
        project_nums = records.distinct().values('Project').count()
        project_nums_20 = records.filter(
            Cost_to_Nav__gt=20
        ).distinct().values('Project').count()
        # suspend_date=0
        #price=tu.get_h_data(i['Code'],autype='None', start=infodate,end=infodate)['close'][0]
        # mv=0
        # turnover_rate=0
        # days_to_settle=0

        for r in records:
            holdings = holdings + r.Holdings

        StockLedge.objects.get_or_create(
            InfoDate=infodate,
            Code=i['Code'],
            Name=name,
            Holdings=holdings,
            Project_Nums=project_nums,
            Project_Nums_20=project_nums_20,
            Suspend_Date= now().date(),
            Price=0,
            MV=0,
            Turnover_Rate=0,
            Days_to_Settle=0,
        )
