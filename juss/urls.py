from django.urls import path
from .views import index_view, SettingView, CustomLoginView

urlpatterns = [
    path('', index_view),
    path('settings/', SettingView.as_view()),
    # path('login/', CustomLoginView.as_view()),
]
