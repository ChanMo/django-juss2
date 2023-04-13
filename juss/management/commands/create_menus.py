from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from juss.models import Menu


class Command(BaseCommand):
    help = 'Create basic menus'

    def handle(self, *args, **options):
        if Menu.objects.count():
            raise CommandError('Menu is not empty.')

        auth_menus = Menu.objects.create(
            name = 'User & Group',
            icon = 'users'
        )
        self.stdout.write(self.style.SUCCESS('Create Auth Menus'))

        Menu.objects.create(
            parent = auth_menus,
            name = 'Groups',
            content_type = ContentType.objects.get(
                app_label='auth', model='group'
            )
        )
        self.stdout.write(self.style.SUCCESS('-- Create Group Menu'))
        auth_app, user_model = settings.AUTH_USER_MODEL.split('.')
        Menu.objects.create(
            parent = auth_menus,
            name = 'Users',
            content_type = ContentType.objects.get(
                app_label=auth_app, model=user_model.lower()
            )
        )
        self.stdout.write(self.style.SUCCESS('-- Create User Menu'))

        system_settings = Menu.objects.create(
            name = 'System Settings',
            icon = 'settings'
        )
        self.stdout.write(self.style.SUCCESS('Create Settings Menu'))
        
        Menu.objects.create(
            parent = system_settings,
            name = 'Admin Menus',
            content_type = ContentType.objects.get(
                app_label='juss', model='menu'),
        )
        self.stdout.write(self.style.SUCCESS('-- Create Juss Menu'))

        Menu.objects.create(name='Dashboard', path='/admin/', icon='bar-chart-2')
        self.stdout.write(self.style.SUCCESS('Create Dashboard Menu'))
