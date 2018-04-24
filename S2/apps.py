from django.apps import AppConfig


class S2Config(AppConfig):
    name = 'S2'
    verbose_name = "二级市场结构化业务"

    def ready(self):
        import S2.signals
