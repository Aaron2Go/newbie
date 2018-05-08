from django.apps import AppConfig


class S1Config(AppConfig):
    name = 'S1'
    verbose_name = "按期统计"

    #def ready(self):
    #    import S2.signals