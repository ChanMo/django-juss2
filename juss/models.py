from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField(_('menu name'), max_length=100)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True,
        related_name='children', verbose_name=_('parent menu'))
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL,
        verbose_name=_('app model'), blank=True, null=True)
    path = models.CharField(_('url'), max_length=200, blank=True, null=True)
    icon = models.SlugField(
        _('icon'), blank=True, null=True,
        help_text='<a target="_blank" href="https://feathericons.com/">Feather Icons</a>')
    groups = models.ManyToManyField(
        Group, blank=True, verbose_name=_('allowed groups'), related_name='juss_menus'
    )

    def __str__(self):
        return self.name

    @property
    def url(self):
        if self.path:
            return self.path
        if self.content_type:
            return f'/admin/{self.content_type.app_label}/{self.content_type.model}/'
        return None

    def has_perms(self, user):
        # 判断用户是否有权限
        if self.content_type and self.groups.count():
            return user.has_perm(f'{self.content_type.app_label}.view_{self.content_type.model}') and user.groups.filter(pk__in=[i.pk for i in self.groups.all()]).exists()
        if self.content_type:
            return user.has_perm(f'{self.content_type.app_label}.view_{self.content_type.model}')
        if self.groups.count():
            return user.groups.filter(pk__in=[i.pk for i in self.groups.all()]).exists()
        if not self.is_leaf_node():
            for child in self.get_children():
                if child.has_perms(user):
                    return True
            return False
        return True
        

    class Meta:
        verbose_name = _('Admin Menu')
        verbose_name_plural = _('Admin Menus')
        
    class MPTTMeta:
        order_insertion_by=['name']
