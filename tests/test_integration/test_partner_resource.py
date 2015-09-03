from time import time

from tests.test_integration.test_case import YolaServiceTestCase


class TestYolaPartners(YolaServiceTestCase):
    """Yola: Partner resource"""

    @classmethod
    def setUpClass(cls):
        super(TestYolaPartners, cls).setUpClass()
        cls.partner = cls._create_partner()
        cls.partner_id = cls.partner['id']
        # There's no way to really delete the test partners we're creating :(

    @classmethod
    def _create_partner(cls, **overrides):
        # can't use a uuid because of 30 char limit:
        unique_id = str(time()).replace('.', '')

        attrs = {
            'id': 'WL_TEST-%s' % unique_id,
            'name': 'TEST',
            'parent_partner_id': 'WL_YOLA',
            'properties': {'website': 'example.com'},
        }
        attrs.update(overrides)

        return cls.service.create_partner(**attrs)

    def test_can_create_partner(self):
        self.assertEqual(self.partner['properties']['website'], 'example.com')

    def test_can_get_partner(self):
        partner = self.service.get_partner(self.partner_id)
        self.assertEqual(partner['name'], 'TEST')

    def test_can_delete_partner(self):
        partner = self._create_partner()
        self.service.delete_partner(partner['id'])
        partner = self.service.get_partner(partner['id'])
        self.assertFalse(partner['is_active'])

    def test_can_update_partner(self):
        partner = self._create_partner(name='Original Name')
        partner = self.service.update_partner(partner['id'], name='New Name')
        self.assertEqual(partner['name'], 'New Name')

    def test_can_list_partners(self):
        response = self.service.list_partners(page_size=1)
        self.assertEqual(len(response['results']), 1)
