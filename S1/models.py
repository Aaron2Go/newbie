from django.db import models
from S2.models import *


# Create your models here.


class ZProject(Project):
    class Meta:
        verbose_name = "项目浏览"
        verbose_name_plural = verbose_name
        proxy = True

    def stock_num(self):
        return NavData.objects.filter(Project=self).count()

    stock_num.short_description = "持有标的数量"

    def stock_num_trade(self):
        return NavData.objects.filter(Project=self, Status='正常').count()

    stock_num_trade.short_description = "正常标的数量"

    def stock_num_sup(self):
        return NavData.objects.filter(Project=self, Status='停牌').count()

    stock_num_sup.short_description = "停牌标的数量"


