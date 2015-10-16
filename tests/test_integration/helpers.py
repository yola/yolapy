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


def create_site(service, user_id=None):
    """Create test site for given user_id.

    If no user id is provided, a test user will be created.
    """
    if not user_id:
        user_id = create_user(service)['id']

    serialized_site = {
        'id': uuid4().hex,
        'cryptoKey': uuid4().hex,
        'user_id': user_id,
        'owner_id': user_id,
        'name': 'My Test Site',
        'version': 62,
        'locale': 'en',
        'properties': {},
        'facebook_page_id': None,
        'site_type': '1',
        'auth_user': None,
        'auth_pass': None,
        'site_template': 'default',
        'base_template': 'SuperFlat_v2',
        'navigation': [],
    }

    return service._create_site(**serialized_site)
