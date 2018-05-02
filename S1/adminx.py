from django.contrib import admin
from S1.models import *  # Project, Branch, Stock
from S2.models import *
import xadmin


class ZZpp(object):
    list_display = [
        'Name',
        'get_zj_nums',
    ]

    def queryset(self):
        qs = super(ZZpp, self).queryset()
        qs = qs.filter(Type='配资类')
        return qs

    def get_zj_nums(self, *args, **kwargs):
        return self.navdata.objects.all().count()

    get_zj_nums.short_description = "底仓数"


xadmin.site.register(ZProject, ZZpp)
