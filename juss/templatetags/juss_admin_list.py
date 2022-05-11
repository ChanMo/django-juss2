from django.template import Library
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.html import format_html

register = Library()

DOT = '.'


@register.simple_tag
def paginator_number(cl, i):
    if i == cl.paginator.ELLIPSIS:
        return format_html('<li><span class="pagination-ellipsis">...</span></li>')
    elif i == cl.page_num:
        return format_html(
            '<li><a class="pagination-link is-current">{}</a></li>',
            i
        )
    else:
        return format_html(
            '<li><a class="pagination-link" href="{}">{}</a></li>',
            cl.get_query_string({PAGE_VAR: i}),
            i
        )
