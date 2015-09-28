from unittest import TestCase

from mock import patch

from yolapy.models.user import User


class UserTestCase(TestCase):

    def setUp(self):
        self.client_patcher = patch('yolapy.models.user.Yola')
        self.addCleanup(self.client_patcher.stop)
        self.client = self.client_patcher.start().return_value
        self.client.username = 'WL_DEFAULT'


class TestUserClient(UserTestCase):

    def test_is_a_yola_client(self):
        self.assertEqual(User().client, self.client)


class TestUserEmail(UserTestCase):

    def setUp(self):
        super(TestUserEmail, self).setUp()
        self.user = User(email='me@example.com')

    def test_is_set_as_a_preference(self):
        self.assertEqual(self.user.preferences['wl_email'], 'me@example.com')

    def test_is_not_destroyed_when_saving(self):
        self.client.create_user.return_value = {
            'email': 'legacy-1234567890asdf1234567890asdf.com'
        }
        self.user.save()
        self.assertEqual(self.user.email, 'me@example.com')


class TestUserLegacyEmail(UserTestCase):

    def setUp(self):
        super(TestUserLegacyEmail, self).setUp()
        self.user = User(name='Jo', surname='Jo', email='me@example.com')
        self.user._legacy_email = 'legacy-1234567890asdf1234567890asdf.com'

    def test_is_used_when_saving(self):
        self.user.save()
        save_call = self.client.create_user.call_args[1]
        self.assertEqual(save_call, {
            'name': 'Jo',
            'surname': 'Jo',
            'partner_id': 'WL_DEFAULT',
            'email': 'legacy-1234567890asdf1234567890asdf.com',
            'preferences': {'wl_email': 'me@example.com'},
        })


class TestUserSave(UserTestCase):

    def test_uses_service_to_create_a_new_user(self):
        user_attrs = {
            'name': 'First',
            'surname': 'Name',
            'email': 'legacy-abc123@example.com',
            'partner_id': 'WL_PARTNER',
            'preferences': {'locale': 'en', 'wl_email': 'email@example.com'},
        }
        user = User(**user_attrs)
        user._legacy_email = 'legacy-abc123@example.com'
        user.save()
        create_user_call = self.client.create_user.call_args[1]
        self.assertEqual(user_attrs, create_user_call)

    def test_generates_a_legacy_email(self):
        User().save()
        create_user_call = self.client.create_user.call_args[1]
        self.assertTrue(create_user_call['email'] is not None)


class TestUserPartnerId(UserTestCase):

    def test_uses_client_config_as_default_partner_id(self):
        self.assertEqual(User().partner_id, 'WL_DEFAULT')

    def test_can_be_set_via_init(self):
        self.assertEqual(User(partner_id='WL_DOG').partner_id, 'WL_DOG')

    def test_can_be_set_via_attribute(self):
        user = User()
        user.partner_id = 'WL_CAT'
        self.assertEqual(user.partner_id, 'WL_CAT')


class TestUserUpdate(UserTestCase):

    def test_updates_all_attributes_passed_in(self):
        user_attrs = {'name': 'Nameski', 'email': 'emailz@example.com'}
        u = User()
        u.update(**user_attrs)
        self.assertEqual(u.name, 'Nameski')
        self.assertEqual(u.email, 'emailz@example.com')
