from django.db import models


# Create your models here.
class NavFile(models.Model):
    Project = models.ForeignKey('S2.Project', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='所属项目')
    InfoDate = models.DateField(verbose_name='口径日期')
    File = models.FileField(upload_to='Upload/Nav_Tables', verbose_name='净值表Excel')
    UploadTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
    Comments = models.TextField(verbose_name='备注', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.Project) +'('+str(self.InfoDate) + ")"

    class Meta:
        verbose_name = '净值表'
        verbose_name_plural = '净值表'


class PlBranch(models.Model):
    File = models.FileField(upload_to='Upload/Branches', verbose_name='数据文件')
    UploadTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
    Comments = models.TextField(verbose_name='备注', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.File) + "(" + str(self.UploadTime) + ")"

    class Meta:
        verbose_name = '经营机构'
        verbose_name_plural = '经营机构'


class PlProject(models.Model):
    File = models.FileField(upload_to='Upload/Projects', verbose_name='数据文件')
    InfoDate = models.DateField(verbose_name='口径日期')
    UploadTime = models.DateTimeField(verbose_name='上传时间', auto_now=True, auto_created=True)
    Comments = models.TextField(verbose_name='备注', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return "(" + str(self.UploadTime) + ")"

    class Meta:
        verbose_name = '项目情况'
        verbose_name_plural = '项目情况'
