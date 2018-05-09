from S2.models import *
from S1.models import *
from django.utils.timezone import now
import tushare as tu  # Tushare 用来获取股票行情信息


def generate_stockledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    StockLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = StockJournal.objects.filter(InfoDate=infodate).distinct().values('Code')
    hist = tu.get_day_all(infodate)
    # 对具体每行数据做操作
    for i in item_list:
        print(i['Code'])
        # 筛选出某行对应的原始数据
        records = StockJournal.objects.filter(InfoDate=infodate, Code=i['Code'])
        # 计算统计指标
        holdings = 0
        name = hist[hist['code'] == i['Code']]['name'].iloc[0]
        project_nums = records.distinct().values('Project').count()
        project_nums_20 = records.filter(
            Cost_to_Nav__gt=20
        ).distinct().values('Project').count()
        # suspend_date=0
        price = hist[hist['code'] == i['Code']]['price'].iloc[0]
        turnover_rate = hist[hist['code'] == i['Code']]['turnover'].iloc[0]
        common_stock_outstanding = hist[hist['code'] == i['Code']]['totals'].iloc[0]
        for r in records:
            holdings = holdings + r.Holdings

        days_to_settle = holdings / turnover_rate / common_stock_outstanding / 1000000
        holdings_to_total = holdings / common_stock_outstanding/10000000
        mv = price * holdings
        # 写入记录到数据表

        print(infodate)
        print(i['Code'])
        print(name)
        print(holdings)
        print(holdings_to_total)
        print(project_nums)
        print(project_nums_20)
        print(now().date())
        print(price)
        print(mv)
        print(turnover_rate)
        print(days_to_settle)
        print(common_stock_outstanding)

        StockLedge.objects.get_or_create(
            InfoDate=infodate,
            Code=i['Code'],
            Name=name,
            Holdings=holdings,
            Holdings_to_Total=0, #holdings_to_total,
            Project_Nums=project_nums,
            Project_Nums_20=project_nums_20,
            Suspend_Date=now().date(),
            Price=price,
            MV=mv,
            Turnover_Rate=turnover_rate,
            Days_to_Settle=0, #days_to_settle,
            Common_Stock_Outstanding=common_stock_outstanding,
        )

def generate_projectledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    ProjectLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = Project.objects.all()
    # 对具体每行数据做操作
    for i in item_list:
        ProjectLedge.objects.get_or_create(
            InfoDate=infodate,
            ID= i.ID,
            Name = i.Name,
            Branch = i.Branch,
            Type = i.Type,
            Approval_Form_Num = i.Approval_Form_Num,
            Issue_Date = i.Issue_Date,
            Duration = i.Duration,
            Amount = i.Amount,
            Leverage_Ratio = i.Leverage_Ratio

        )