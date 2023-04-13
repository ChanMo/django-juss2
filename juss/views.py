import uuid
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Setting
from .forms import SettingForm


class SettingView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'juss.can_edit_setting'
    model = Setting
    form_class = SettingForm
    template_name = 'juss/setting.html'
    success_url = '/admin/settings/'
    success_message = '更新成功'

    def get_object(self):
        obj, created = Setting.objects.get_or_create()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {**context, **admin.site.each_context(self.request)}
        context['title'] = '系统设置'
        return context


@staff_member_required
def index_view(request):
    context = admin.site.each_context(request)
    return render(request, 'admin/index.html', context)


class CustomLoginView(LoginView):
    template_name = 'admin/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())

        token = str(uuid.uuid4())
        self.request.session['sso_token'] = token
        user = form.get_user()
        user.token = token
        user.save()

        return HttpResponseRedirect(self.get_success_url())


