import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'server.settings')
app = Celery("server", backend="django-db")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
