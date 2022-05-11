from django.forms import ModelForm
from .widgets import AdminTextInputWidget, AdminTextareaWidget, ColorChoiceWidget, AdminModelChoiceWidget, AdminURLFieldWidget
from .models import Setting


class SettingForm(ModelForm):
    class Meta:
        model = Setting
        fields = ['site_title', 'logo', 'promotion_image', 'wx_appid', 'wx_secret']
        widgets = {
            'site_title': AdminTextInputWidget(),
            'wx_appid': AdminTextInputWidget(),
            'wx_secret': AdminTextInputWidget()
        }
