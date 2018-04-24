from django.apps import AppConfig


class S2Config(AppConfig):
    name = 'S2'
    verbose_name = "数据维护"

    #def ready(self):
    #    import S2.signals
