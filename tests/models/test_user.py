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


class TestUserSave(UserTestCase):

    def test_uses_service_to_create_a_new_user(self):
        user_attrs = {
            'name': 'First',
            'surname': 'Name',
            'email': 'email@example.com',
            'partner_id': 'WL_PARTNER',
            'preferences': {'locale': 'en'},
        }
        user = User(**user_attrs)
        user.save()
        create_user_call = self.client.create_user.call_args[1]
        self.assertEqual(user_attrs, create_user_call)


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
