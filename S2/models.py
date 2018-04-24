from django.db import models


class Branch(models.Model):
    Name = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name='经营机构')
    Area = models.CharField(max_length=10, verbose_name='地域')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "经营机构"
        verbose_name_plural = "经营机构"


class Project(models.Model):
    ID = models.CharField(max_length=10, verbose_name='编号', primary_key=True, unique=True)
    Name = models.CharField(max_length=50, verbose_name='名称')
    Branch = models.ForeignKey("Branch", null=True, blank=True, on_delete=models.SET_NULL,
                               verbose_name='经营机构')
    Project_Type = (
        ('Z', '直投类'),
        ('P', '配资类'),
    )
    Type = models.CharField(max_length=1, choices=Project_Type, verbose_name='类型')
    Approval_Form_Num = models.CharField(max_length=150, verbose_name='审批单号')
    Issue_Date = models.DateField(verbose_name='发行日期')
    Duration = models.IntegerField(verbose_name='期限')
    Amount = models.IntegerField(verbose_name='金额')
    Leverage_Ratio = models.FloatField(verbose_name='杠杆率')

    def __str__(self):
        return "(" + self.ID + ")" + self.Name

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"


class Guarantor(models.Model):
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    Project = models.ForeignKey("Project", null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name='项目')

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "差额补足人"
        verbose_name_plural = "差额补足人"


class Adviser(models.Model):
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    Project = models.ForeignKey("Project", null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name='项目')

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "投资顾问"
        verbose_name_plural = "投资顾问"


class Posterior(models.Model):
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    Project = models.ForeignKey("Project", null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name='项目')

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "劣后级"
        verbose_name_plural = "劣后级"


class NavData(models.Model):
    # Project = models.ForeignKey('Project', null=True ,blank=True, on_delete=models.SET_NULL, verbose_name='项目')
    # InfoDate = models.DateField(verbose_name='口径日期')
    Code = models.CharField(max_length=10, verbose_name='编号')
    Name = models.CharField(max_length=50, verbose_name='名称')
    Holdings = models.IntegerField(verbose_name='持股数量', null = True)
    Purchase_Price = models.FloatField(verbose_name='成本价', null = True)
    Costs = models.FloatField(verbose_name='成本', null = True)
    Cost_to_NAV = models.FloatField(verbose_name='成本占净值比例(%)', null = True)
    Market_Price = models.FloatField(verbose_name='收盘价', null = True)
    Market_Value = models.FloatField(verbose_name='市值', null = True)
    Market_Value_to_NAV = models.FloatField(verbose_name='市值占净值比例(%)', null = True)
    Valuation = models.FloatField(verbose_name='估值', null = True)
    Status = models.CharField(max_length=10, verbose_name='交易状态', null = True)
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.Code + ")"

    class Meta:
        verbose_name = 'A股持仓'
        verbose_name_plural = 'A股持仓'


class NavFile(models.Model):
    # Project = models.ForeignKey('Project',null=True , blank=True, on_delete=models.SET_NULL, verbose_name='项目')
    # InfoDate = models.DateField(verbose_name='口径日期', primary_key=True)
    Filename = models.CharField(max_length=50, verbose_name='文件名称')
    File = models.FileField(upload_to='Nav_Tables', verbose_name='数据文件')
    FileType = models.CharField(max_length=10, verbose_name='文件类型')
<<<<<<< HEAD
    UploadedDateTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
=======
    UploadedDateTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, primary_key = True)
>>>>>>> b6270b3e89966c25abb55f1b3e041a61f05db296
    LastModifiedDateTime = models.DateTimeField(verbose_name='上次修改时间')
    ModifiedTimes = models.IntegerField(verbose_name='修改次数')
    Comments = models.TextField(verbose_name='备注')
    objects = models.Manager()

    def __str__(self):
        return "(" + str(self.UploadedDateTime) + ")"

    class Meta:
        verbose_name = '净值表'
        verbose_name_plural = '净值表'

