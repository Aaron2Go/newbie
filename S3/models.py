from django.db import models


# Create your models here.
class NavFile(models.Model):
    Project = models.ForeignKey('S2.Project', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='项目')
    InfoDate = models.DateField(verbose_name='口径日期', primary_key=True)
    # Filename = models.CharField(max_length=50, verbose_name='文件名称')
    File = models.FileField(upload_to='Upload\Nav_Tables', verbose_name='数据文件')
    # FileType = models.CharField(max_length=10, verbose_name='文件类型')
    UploadTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
    # LastModifiedDateTime = models.DateTimeField(verbose_name='上次修改时间')
    # ModifiedTimes = models.IntegerField(verbose_name='修改次数')
    Comments = models.TextField(verbose_name='备注', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.Project) +'('+str(self.InfoDate) + ")"

    class Meta:
        verbose_name = '净值表'
        verbose_name_plural = '净值表'


class PlBranch(models.Model):
    File = models.FileField(upload_to='Upload\Branches', verbose_name='数据文件')
    UploadTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
    Comments = models.TextField(verbose_name='备注', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.File) + "(" + str(self.UploadTime) + ")"

    class Meta:
        verbose_name = '经营机构'
        verbose_name_plural = '经营机构'


class PlProject(models.Model):
    InfoDate = models.DateField(verbose_name='口径日期', primary_key=True)
    File = models.FileField(upload_to='Upload\Projects', verbose_name='数据文件')
    UploadTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
    Comments = models.TextField(verbose_name='备注', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return "(" + str(self.UploadTime) + ")"

    class Meta:
        verbose_name = '项目情况'
        verbose_name_plural = '项目情况'
