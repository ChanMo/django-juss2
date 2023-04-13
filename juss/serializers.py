from rest_framework.serializers import ModelSerializer
from .models import Setting


class SettingSerializer(ModelSerializer):
    class Meta:
        model = Setting
        fields = ('site_title', 'logo', 'promotion_image')
