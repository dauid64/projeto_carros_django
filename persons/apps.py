from django.apps import AppConfig


class PersonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persons'

    def ready(self, *args, **kwargs) -> None:
            import persons.signals
            super_ready = super().ready(*args, **kwargs)
            return super_ready