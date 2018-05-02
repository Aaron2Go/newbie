from django.db import models


class Branch(models.Model):
    Name = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name='经营机构')
    Area = models.CharField(max_length=10, verbose_name='地域')
    objects = models.Manager()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "经营机构"
        verbose_name_plural = "经营机构"


class Project(models.Model):
    ID = models.CharField(max_length=10, verbose_name='编号', primary_key=True, unique=True)
    Name = models.CharField(max_length=50, verbose_name='项目名称')
    Branch = models.ForeignKey("Branch", null=True, on_delete=models.CASCADE,
                               verbose_name='经营机构')
    Project_Type = (
        ('直投类', '直投类'),
        ('配资类', '配资类'),
    )
    Type = models.CharField(max_length=3,choices=Project_Type, verbose_name='类型')
    Approval_Form_Num = models.CharField(max_length=150, verbose_name='审批单号')
    Issue_Date = models.DateField(verbose_name='发行日期')
    Duration = models.IntegerField(verbose_name='期限')
    Amount = models.IntegerField(verbose_name='金额')
    Leverage_Ratio = models.FloatField(verbose_name='杠杆率')
    objects = models.Manager()

    def __str__(self):
        return "(" + self.ID + ")" + self.Name

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"


class Guarantor(models.Model):
    Project = models.ManyToManyField("Project", verbose_name='项目')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "差额补足人"
        verbose_name_plural = "差额补足人"


class Adviser(models.Model):
    Project = models.ManyToManyField("Project", verbose_name='项目')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "投资顾问"
        verbose_name_plural = "投资顾问"


class Posterior(models.Model):
    Project = models.ManyToManyField("Project", verbose_name='项目')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "劣后级"
        verbose_name_plural = "劣后级"


class NavData(models.Model):
    Project = models.ForeignKey(Project,related_name='navdata',null=True ,blank=True, on_delete=models.CASCADE, verbose_name='项目')
    InfoDate = models.DateField(verbose_name='口径日期')
    Code = models.CharField(max_length=10, verbose_name='证券代码')
    Name = models.CharField(max_length=50, verbose_name='证券简称')
    Holdings = models.IntegerField(verbose_name='持股数量（股）')
    Purchase_Price = models.FloatField(verbose_name='成本价')
    Costs = models.FloatField(verbose_name='持有成本')
    Cost_to_NAV = models.FloatField(verbose_name='成本占净值比例(%)')
    Market_Price = models.FloatField(verbose_name='当日市价')
    Market_Value = models.FloatField(verbose_name='当日市值')
    Market_Value_to_NAV = models.FloatField(verbose_name='市值占净值比例(%)')
    Valuation = models.FloatField(verbose_name='估值增值')
    Status = models.CharField(max_length=10, verbose_name='交易状态')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.Code + ")"

    class Meta:
        verbose_name = '底仓详情'
        verbose_name_plural = '底仓详情'

