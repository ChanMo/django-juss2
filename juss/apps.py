from django.apps import AppConfig
from django.contrib.admin import apps


class JussConfig(AppConfig):
    name = 'juss'

class JussAdminConfig(apps.AdminConfig):
    default_site = 'juss.admin.JussAdminSite'
