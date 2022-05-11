default_app_config='juss.apps.JussConfig'


def get_setting():
    from .models import Setting

    obj, created = Setting.objects.get_or_create()
    return obj
