from django.apps import AppConfig


class S3Config(AppConfig):
    name = 'S3'
    verbose_name = "数据录入"

    def ready(self):
        import S3.signals
