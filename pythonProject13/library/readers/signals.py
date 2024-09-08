from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group


def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Librarians')
    Group.objects.get_or_create(name='Admins')


post_migrate.connect(create_groups)