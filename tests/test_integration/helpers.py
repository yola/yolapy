from uuid import uuid4


def create_user(service, **custom_attrs):
    """Create test user with default attributes.

    Override default attributes by passing keyword arguments.
    """
    attrs = {
        'email': 'test+%s@yola.com' % uuid4().hex,
        'name': 'John',
        'surname': 'Smith',
        'partner_id': 'WL_YOLA',
        'preferences': {},
    }
    attrs.update(custom_attrs)
    return service.create_user(**attrs)
