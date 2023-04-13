from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'show_icon', 'show_groups')
    list_display_links = ('indented_title',)
    search_fields = ('name',)

    @admin.display(description='授权分组')
    def show_groups(self, obj):
        return ','.join([i.name for i in obj.groups.all()])

    @admin.display(description='图标')
    def show_icon(self, obj):
        if not obj.icon:
            return None
        
        return format_html(
            '<span class="icon">'
            '<i data-feather="{}" width="18" height="18"></i></span>',
            obj.icon
        )
