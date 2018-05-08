from S2.models import StockJournal
from S1.models import StockLedge
from django.utils.timezone import now
<<<<<<< HEAD

# import tushare as tu
=======
import tushare as tu # Tushare 用来获取股票行情信息

>>>>>>> fa19428fa6a93d2ef0d15f5b1d5762c7ce14bafd

def generate_stockledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    StockLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = StockJournal.objects.filter(InfoDate=infodate).distinct().values('Code')
    # 对具体每行数据做操作
    for i in item_list:
        # 筛选出某行对应的原始数据
        records = StockJournal.objects.filter(InfoDate=infodate, Code=i['Code'])
        # 计算统计指标
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
        # 写入记录到数据表
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
