# Django Juss Theme v2

使用Bulma.css重写Admin模板


## Quick Start

### Install


### Update Settings.py

```
INSTALLED_APPS = [
...
'juss',
'juss.apps.JussAdminConfig',
#'django.contrib.admin',
...
]
```

### Custom Left Menus

Edit `settings.py`

```
JUSS_MENU = [
    {'label': 'Default', 'children': [
        {'label': 'Dashboard', 'path': '/admin/'},
    ]},
    {'label': 'Auth && Permissions', 'children': [
        {'model': 'auth.user'},
        {'model': 'auth.group'},
    ]},
]

```

### Use JussFormStyle to My Admin Class

Edit `blogs/admin.py`

```
from django.contrib import admin
from juss.admin import JussAdminMixin
from blogs.models import Blog

@admin.register(Blog)
class BlogAdmin(JussAdminMixin, admin.ModelAdmin):
    ...
```

## Todo

* [ ] Multiple Color Palette
* [ ] Multiple Login Page
