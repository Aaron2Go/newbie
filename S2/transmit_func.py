from S2.models import *
from S1.models import *
from django.utils.timezone import now
import tushare as tu  # Tushare 用来获取股票行情信息
from django.db.models import Sum, Avg, Max


def generate_stockledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    StockLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = StockJournal.objects.filter(InfoDate=infodate).distinct().values('Code')
    hist = tu.get_day_all(infodate)
    # 对具体每行数据做操作
    for i in item_list:
        # 筛选出某行对应的原始数据
        records = StockJournal.objects.filter(InfoDate=infodate, Code=i['Code'])
        # 计算统计指标
        suspend_date = now().date()
        price = hist[hist['code'] == i['Code']]['price'].iloc[0]

        holdings = records.aggregate(vl=Sum('Holdings'))['vl']
        turnover_rate = hist[hist['code'] == i['Code']]['turnover'].iloc[0]
        common_stock_outstanding = hist[hist['code'] == i['Code']]['totals'].iloc[0]
        days_to_settle = holdings / turnover_rate / common_stock_outstanding / 1000000
        holdings_to_total = holdings / common_stock_outstanding / 10000000
        mv = price * holdings
        # 写入记录到数据表

        print(now().date())
        print(price)
        print(mv)
        print(turnover_rate)
        print(days_to_settle)
        print(common_stock_outstanding)

        StockLedge.objects.get_or_create(
            InfoDate=infodate,
            Code=i['Code'],
            Name=hist[hist['code'] == i['Code']]['name'].iloc[0],
            Holdings=records.aggregate(vl=Sum('Holdings'))['vl'],
            Holdings_to_Total=holdings_to_total,
            Project_Nums=records.distinct().values('Project').count(),
            Project_Nums_20=records.filter(Cost_to_Nav__gt=20).distinct().values('Project').count(),
            Suspend_Date=suspend_date,
            Price=hist[hist['code'] == i['Code']]['price'].iloc[0],
            MV=mv,
            Turnover_Rate=turnover_rate,
            Days_to_Settle=0,  # days_to_settle,
            Common_Stock_Outstanding=common_stock_outstanding,
        )


def generate_projectledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    ProjectLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = Project.objects.all()
    # 对具体每行数据做操作
    for i in item_list:
        if StockJournal.objects.filter(Project=i, InfoDate=infodate).count() != 0:
            ProjectLedge.objects.get_or_create(
                InfoDate=infodate,
                Project=i,
                Branch=i.Branch,
                Type=i.Type,
                Approval_Form_Num=i.Approval_Form_Num,
                Issue_Date=i.Issue_Date,
                Duration=i.Duration,
                Amount=i.Amount,
                Leverage_Ratio=i.Leverage_Ratio,
                Stock_Num=StockJournal.objects.filter(Project=i, InfoDate=infodate).count(),
                Stock_Num_ST=StockJournal.objects.filter(Project=i, InfoDate=infodate, Name='%ST%').count(),
                Stock_Num_Suspend=StockJournal.objects.filter(Project=i, InfoDate=infodate, Status='停牌').count(),
                First_Record_Date=NavJournal.objects.filter(Project=i).earliest('InfoDate').InfoDate,
                Current_Nav=NavJournal.objects.filter(Project=i, InfoDate=infodate).last().NetValue,
                Nav_Warn=0,
                Nav_Stop=0,
            )


def generate_branchledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    BranchLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = Branch.objects.all()
    # 对具体每行数据做操作
    for i in item_list:
        if ProjectLedge.objects.filter(Branch=i, InfoDate=infodate).aggregate(vl=Sum('Amount'))['vl'] is not None:
            BranchLedge.objects.get_or_create(
                InfoDate=infodate,
                Branch=i,
                Amounts_Total=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate).aggregate(vl=Sum('Amount'))['vl'],
                Amounts_Avg=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate).aggregate(vl=Avg('Amount'))['vl'],
                Project_Num=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate).count(),
                Project_Num_ST=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate, Stock_Num_ST__gt=0).count(),
                Project_Num_Suspend=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate,
                                                                Stock_Num_Suspend__gt=0).count(),
                Project_Num_Normal=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate).count(),
                Project_Num_Warn=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate, Nav_Warn__lte=0).count(),
                Project_Num_Stop=ProjectLedge.objects.filter(Branch=i, InfoDate=infodate, Nav_Stop__lte=0).count(),
                Stock_Num=StockJournal.objects.filter(Project__Branch=i, InfoDate=infodate).distinct().values(
                    'Code').count(),
                Stock_Num_Suspend=StockJournal.objects.filter(Project__Branch=i, InfoDate=infodate,
                                                              Status='停牌').distinct().values('Code').count(),
                Stock_Num_ST=StockJournal.objects.filter(Project__Branch=i, InfoDate=infodate,
                                                         Name='%ST%').distinct().values('Code').count(),
                Days_Settle_Max=0,
                # StockJournal.objects.filter(Project__Branch=i, InfoDate=infodate).aggregate(vl=Max('Amount'))['vl'],
                Days_Settle_Avg=0,
                Days_Settle_Mid=0,
            )

def generate_ledge(infodate):
    # 清除infodate对于的所有统计数据，以重算所有
    StockLedge.objects.filter(InfoDate=infodate).delete()
    # 获取每行的首列
    item_list = StockJournal.objects.filter(InfoDate=infodate).distinct().values('Code')
    # 对具体每行数据做操作
    for i in item_list:
        pass