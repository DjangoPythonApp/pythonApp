from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "category"

    # Because Django must load signals when app starts.
    def ready(self):
        import category.signals
