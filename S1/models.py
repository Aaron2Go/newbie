from django.db import models
from S2.models import *
# Create your models here.


class ZProject(Project):
    class Meta:
        verbose_name = "项目浏览"
        verbose_name_plural = verbose_name
        proxy = True


