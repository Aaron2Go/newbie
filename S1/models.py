from django.db import models
from S2.models import *


# Create your models here.

#class BranchLedge(models.Model):
    #Name=
    #InfoDate=
    #Amounts_Total=
    #Amounts_Avg=
    #Project_Num=
    #Project_Num_ST=
    #Project_Num_Suspend=
    #Project_Num_Normal=
    #Stock_Num=
    #Stock_Num_Suspend=
    #Stock_Num_Trade=
    #Stock_Num_ST=
    #Days_Settle_Max=
    #Days_Settle_Min=
    #Days_Settle_Avg=
    #Days_Settle_Mid=



#    objects = models.Manager()
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name
#    unique_together = [
#        'Name',
#        'InfoDate',
#    ]

#class ProjectLedge(Project):
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name



class StockLedge(models.Model):
    InfoDate = models.DateField(verbose_name='口径日期')
    Code = models.CharField(max_length=10, verbose_name='证券代码')
    Name = models.CharField(max_length=50, verbose_name='证券简称')
    Holdings = models.IntegerField(verbose_name='持股数量（股）')
    Project_Nums = models.IntegerField(verbose_name='项目数')
    Project_Nums_20 = models.IntegerField(verbose_name='项目（超20%）数')
    Suspend_Date = models.DateField(verbose_name='停牌日期')
    Price = models.DecimalField(verbose_name='市价', max_digits=5, decimal_places=2)
    MV = models.DecimalField(verbose_name='市值', max_digits=12, decimal_places=2)
    Turnover_Rate = models.DecimalField(verbose_name='换手率', max_digits=5, decimal_places=2)
    Days_to_Settle = models.DecimalField(verbose_name='处置天数', max_digits=5, decimal_places=2)
    #Related_Projects = models.ManyToManyField(S2.Project, verbose_name='关联项目')
    objects = models.Manager()
    class Meta:
        verbose_name = "按项目统计"
        verbose_name_plural = verbose_name
        unique_together = ("InfoDate", "Code")


#class GuarantorLedge(models.Model):
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name



#class AdviserLedge(models.Model):
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name


#class PosteriorLedge(models.Model):
#    class Meta:
#        verbose_name = "按项目统计"
#        verbose_name_plural = verbose_name
