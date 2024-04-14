from __future__ import absolute_import
import os
from celery import Celery

from app.app import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery("app")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'Asia/Almaty'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {}
