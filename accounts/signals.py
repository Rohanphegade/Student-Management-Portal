from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_manager_group(sender, **kwargs):
    """
    This function runs AFTER migrations.
    Safe place to access database.
    """

    manager_group, created = Group.objects.get_or_create(name='Manager')

    # Models Manager can fully control
    allowed_models = [
        'student',
        'lead',
        'document',
    ]

    permissions = Permission.objects.filter(
        content_type__model__in=allowed_models
    )

    manager_group.permissions.set(permissions)

    print("✔ Manager group ensured with permissions")
