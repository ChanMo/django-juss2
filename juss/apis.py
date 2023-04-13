from django.urls import path
from rest_framework.generics import RetrieveAPIView
from .serializers import SettingSerializer
from .models import Setting
from . import get_setting


class SettingView(RetrieveAPIView):
    serializer_class = SettingSerializer
    model = Setting

    def get_object(self):
        return get_setting()


urlpatterns = [
    path('setting/', SettingView.as_view())
]
