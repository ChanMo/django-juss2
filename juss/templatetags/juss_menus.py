import re
from django import template
from juss.models import Menu

register = template.Library()

@register.filter
def has_menu_perms(menu, user):
    return menu.has_perms(user)


@register.filter
def active_menu(target, current):
    " 判断当前选中菜单 "
    if target == '/admin/':
        return re.match('^.*\/admin\/(\?.*)?$', current)
    elif target:
        m = target + '(\d*/change/|add|\d*/delete/|\d*/history)'
        return current == target or re.findall(m, current)
    else:
        return False


@register.inclusion_tag('juss/left_menu.html', takes_context=True)
def juss_left_menus(context):
    user = context['request'].user # current user
    menus = Menu.objects.filter(parent__isnull=True)
    return {
        'user': user,
        'menus': menus,
        'request': context['request']
    }
