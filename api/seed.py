"""Seed data to the db."""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Django
import django
django.setup()

# User's Model
from apps.users.models import User, Manager


big_boss = User.objects.create_user(
    username='bigboss',
    first_name='Big',
    last_name='Boss',
    email='bigboss@hitmen.com',
    password='bigbosspass',
    is_staff=True,
    is_superuser=True,
)
big_boss.save()

for i in range(1,4):
    user_manager = User.objects.create_user(
        username=f'manager{i}',
        first_name='Manager',
        last_name=f'{i}',
        email=f'manager{i}@hitmen.com',
        password='managerpass',
        is_manager=True,
    )
    user_manager.save()
    manager = Manager.objects.create(user=user_manager)
    manager.save()

for i in range(1,10):
    hitman = User.objects.create_user(
        username=f'hitman{i}',
        first_name='hitman',
        last_name=f'{i}',
        email=f'hitman{i}@hitmen.com',
        password='hitmanpass',
    )
    hitman.save()
