from django.apps import AppConfig


class S1Config(AppConfig):
    name = 'S1'
    verbose_name = "数据浏览"

    #def ready(self):
    #    import S2.signals