from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model # If used custom user model
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model() # NOQA
        username = getattr(settings, 'ADMIN_USERNAME', 'admin')

        if User.objects.filter(username=username).exists():
            email = getattr(settings, 'ADMIN_EMAIL', 'admin@baykar.com')
            password = getattr(settings, 'ADMIN_PASSWORD', 'baykar12345@!')
            User.objects.create_superuser(username=username, email=email, password=password)
            print('Admin user created.')
        else:
            print('Already an admin user exists.')

