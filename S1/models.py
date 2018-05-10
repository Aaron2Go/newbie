from django.db import models
from S2.models import *


# Create your models here.

class BranchLedge(models.Model):
    InfoDate = models.DateField(verbose_name='口径日期')
    Branch = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE, verbose_name='经营机构')
    Amounts_Total = models.IntegerField(verbose_name='总金额',null=True)
    Amounts_Avg = models.IntegerField(verbose_name='平均金额',null=True)
    Project_Num = models.IntegerField(verbose_name='项目数',null=True)
    Project_Num_ST = models.IntegerField(verbose_name='含ST项目数',null=True)
    Project_Num_Suspend = models.IntegerField(verbose_name='含停牌项目数',null=True)
    Project_Num_Normal = models.IntegerField(verbose_name='正常项目数',null=True)
    Project_Num_Warn = models.IntegerField(verbose_name='破预警项目数',null=True)
    Project_Num_Stop = models.IntegerField(verbose_name='破预警项目数',null=True)
    Stock_Num = models.IntegerField(verbose_name='标的数量',null=True)
    Stock_Num_Suspend = models.IntegerField(verbose_name='停牌标的数',null=True)
    Stock_Num_ST = models.IntegerField(verbose_name='ST标的数',null=True)
    Days_Settle_Max = models.DecimalField(verbose_name='最大处置天数', max_digits=5, decimal_places=2,null=True)
    Days_Settle_Avg = models.DecimalField(verbose_name='平均处置天数', max_digits=5, decimal_places=2,null=True)
    Days_Settle_Mid = models.DecimalField(verbose_name='中值处置天数', max_digits=5, decimal_places=2,null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "按经营机构统计"
        verbose_name_plural = verbose_name
        unique_together = [
            'Branch',
            'InfoDate',
        ]


class ProjectLedge(models.Model):
    InfoDate = models.DateField(verbose_name='口径日期')
    Project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    Branch = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE, verbose_name='经营机构')
    Project_Type = (('直投类', '直投类'), ('配资类', '配资类'),)
    Type = models.CharField(max_length=3, choices=Project_Type, verbose_name='类型')
    Approval_Form_Num = models.CharField(max_length=150, verbose_name='审批单号')
    Issue_Date = models.DateField(verbose_name='发行日期')
    Duration = models.IntegerField(verbose_name='期限')
    Amount = models.IntegerField(verbose_name='金额')
    Leverage_Ratio = models.DecimalField(verbose_name='杠杆率', max_digits=3, decimal_places=1)
    objects = models.Manager()
    Stock_Num = models.IntegerField(verbose_name='标的数量')
    Stock_Num_ST = models.IntegerField(verbose_name='ST标的数')
    Stock_Num_Suspend = models.IntegerField(verbose_name='停牌标的数')
    First_Record_Date = models.DateField(verbose_name='最早记录日期')
    Current_Nav = models.DecimalField(verbose_name='当期单位净值', max_digits=6, decimal_places=4)
    Nav_Warn = models.DecimalField(verbose_name='净值预警差值', max_digits=6, decimal_places=4)
    Nav_Stop = models.DecimalField(verbose_name='净值止损差值', max_digits=6, decimal_places=4)

    class Meta:
        verbose_name = "按项目统计"
        verbose_name_plural = verbose_name
        unique_together = [
            'Project',
            'InfoDate',
        ]

class StockLedge(models.Model):
    InfoDate = models.DateField(verbose_name='口径日期')
    Code = models.CharField(max_length=10, verbose_name='证券代码')
    Name = models.CharField(max_length=50, verbose_name='证券简称')
    Holdings = models.IntegerField(verbose_name='持股数量（股）')
    Holdings_to_Total = models.DecimalField(verbose_name='总股本占比', max_digits=5, decimal_places=2)
    Project_Nums = models.IntegerField(verbose_name='项目数')
    Project_Nums_20 = models.IntegerField(verbose_name='项目（超20%）数')
    Suspend_Date = models.DateField(verbose_name='停牌日期', null=True, blank=True)
    Price = models.DecimalField(verbose_name='市价', max_digits=5, decimal_places=2)
    MV = models.DecimalField(verbose_name='市值', max_digits=12, decimal_places=2)
    Turnover_Rate = models.DecimalField(verbose_name='换手率', max_digits=5, decimal_places=2)
    Days_to_Settle = models.DecimalField(verbose_name='处置天数', max_digits=5, decimal_places=2)
    Common_Stock_Outstanding = models.DecimalField(verbose_name='总股本（亿）', max_digits=12, decimal_places=2)
    # Related_Projects = models.ManyToManyField(S2.Project, verbose_name='关联项目')
    objects = models.Manager()

    class Meta:
        verbose_name = "按标的统计"
        verbose_name_plural = verbose_name
        unique_together = ("InfoDate", "Code")

    def __str__(self):
        return self.Name + ' ' + self.Code + "(" + str(self.InfoDate) + ")"

# class GuarantorLedge(models.Model):
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name


class AdviserLedge(models.Model):
    InfoDate = models.DateField(verbose_name='口径日期')
    Name = models.CharField(max_length=20, verbose_name='名称')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    #Project_Num=


    class Meta:
        verbose_name = "按项目统计"
        verbose_name_plural = verbose_name


# class PosteriorLedge(models.Model):
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name
