def is_admin(user):
    return user.is_superuser


def is_manager(user):
    return user.groups.filter(name='Manager').exists()


def is_admin_or_manager(user):
    return is_admin(user) or is_manager(user)
