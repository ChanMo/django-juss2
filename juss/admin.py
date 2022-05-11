import copy
import logging
from django.contrib.admin import AdminSite
from django import forms
from django.db import models
from django.contrib.admin.options import get_ul_class
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from mptt.models import TreeForeignKey
from django.forms.widgets import CheckboxSelectMultiple, SelectMultiple
from . import widgets

logger = logging.getLogger(__name__)

FORMFIELD_FOR_DBFIELD_DEFAULTS = {
    models.DateTimeField: {
        'form_class': forms.SplitDateTimeField,
        'widget': widgets.AdminSplitDateTime
    },
    # models.DateTimeField: {'widget': widgets.AdminSimpleDateTimeInputWidget},
    models.DateField: {'widget': widgets.AdminDateWidget},
    models.TimeField: {'widget': widgets.AdminTimeWidget},
    models.TextField: {'widget': widgets.AdminTextareaWidget},
    models.URLField: {'widget': widgets.AdminURLFieldWidget},
    models.IntegerField: {'widget': widgets.AdminIntegerFieldWidget},
    models.DecimalField: {'widget': widgets.AdminIntegerFieldWidget},
    models.BigIntegerField: {'widget': widgets.AdminBigIntegerFieldWidget},
    models.CharField: {'widget': widgets.AdminTextInputWidget},
    models.ImageField: {'widget': widgets.AdminImageWidget},
    models.FileField: {'widget': widgets.AdminFileWidget},
    models.EmailField: {'widget': widgets.AdminEmailInputWidget},
    models.UUIDField: {'widget': widgets.AdminUUIDInputWidget},
    models.ForeignKey: {'widget': widgets.AdminModelChoiceWidget},
    models.BooleanField: {'widget': widgets.AdminBooleanChoiceWidget},

    TreeForeignKey: {'widget': widgets.AdminModelChoiceWidget},
}


class JussAdminMixin:

    def __init__(self, model, admin_site):
        overrides = copy.deepcopy(FORMFIELD_FOR_DBFIELD_DEFAULTS)
        for k, v in self.formfield_overrides.items():
            overrides.setdefault(k, {}).update(v)
        self.formfield_overrides = overrides
        super().__init__(model, admin_site)

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        kwargs['widget'] = widgets.AdminModelChoiceWidget
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if not db_field.remote_field.through._meta.auto_created:
            return None
        db = kwargs.get('using')

        # kwargs['widget'] = widgets.AutocompleteSelectMultiple(
        #     db_field.remote_field, self.admin_site, using=db)

        if 'widget' not in kwargs:
            autocomplete_fields = self.get_autocomplete_fields(request)
            if db_field.name in autocomplete_fields:
                kwargs['widget'] = widgets.AutocompleteSelectMultiple(
                    db_field.remote_field, self.admin_site, using=db)
            elif db_field.name in self.raw_id_fields:
                kwargs['widget'] = widgets.ManyToManyRawIdWidget(
                    db_field.remote_field, self.admin_site, using=db)
            elif db_field.name in [*self.filter_vertical, *self.filter_horizontal]:
                kwargs['widget'] = widgets.FilteredSelectMultiple(
                    db_field.verbose_name,
                    db_field.name in self.filter_vertical
                )

        if 'queryset' not in kwargs:
            queryset = self.get_field_queryset(db, db_field, request)
            if queryset is not None:
                kwargs['queryset'] = queryset

        form_field = db_field.formfield(**kwargs)

        if (isinstance(form_field.widget, SelectMultiple) and
                not isinstance(form_field.widget, (CheckboxSelectMultiple, widgets.AutocompleteSelectMultiple))):
            msg = _(
                'Hold down “Control”, or “Command” on a Mac, to select more than one.')
            help_text = form_field.help_text
            form_field.help_text = format_lazy(
                '{} {}', help_text, msg) if help_text else msg
        return form_field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        db = kwargs.get('using')

        if 'widget0' not in kwargs:
            if db_field.name in self.get_autocomplete_fields(request):
                # kwargs['widget'] = AutocompleteSelect(db_field.remote_field, self.admin_site, using=db)
                pass
            elif db_field.name in self.raw_id_fields:
                kwargs['widget'] = widgets.ForeignKeyRawIdWidget(
                    db_field.remote_field, self.admin_site, using=db)
            elif db_field.name in self.radio_fields:
                kwargs['widget'] = widgets.AdminRadioSelect(attrs={
                    'class': get_ul_class(self.radio_fields[db_field.name]),
                })
                kwargs['empty_label'] = _('None') if db_field.blank else None

        if 'queryset' not in kwargs:
            queryset = self.get_field_queryset(db, db_field, request)
            if queryset is not None:
                kwargs['queryset'] = queryset

        return db_field.formfield(**kwargs)


class JussAdminSite(AdminSite):
    enable_avatar = True
    password_change_template = "juss/password_change.html"
    logout_template = "juss/logout.html"
    login_template = 'juss/login2.html'

    def each_context(self, request):
        context = super().each_context(request)
        context['enable_avatar'] = self.enable_avatar
        return context
