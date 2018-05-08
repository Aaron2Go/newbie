from django.apps import AppConfig


class S3Config(AppConfig):
    name = 'S3'
    verbose_name = "从excel导入"

    def ready(self):
        import S3.signals
