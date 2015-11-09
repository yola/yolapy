from tests.test_integration.test_case import YolaServiceTestCase

from tests.test_integration.helpers import create_partner, create_user


class TestYolaSubscription(YolaServiceTestCase):
    """Yola: Subscription resource"""

    @classmethod
    def setUpClass(cls):
        super(TestYolaSubscription, cls).setUpClass()
        cls.partner = create_partner(cls.service, properties={
            'website': 'example.com',
            'available_subscription_types': ['wl_basic', 'wl_lite']
        })

        user = create_user(cls.service, partner_id=cls.partner['id'])
        cls.subscription = cls.service.create_subscription(
            'wl_basic', user['id'], {'foo': 'bar'})

    def test_can_create_subscriptions(self):
        self.assertEqual(self.subscription['status'], 'active')

    def test_can_list_subscriptions(self):
        subs = self.service.list_subscriptions()['results']
        self.assertTrue(len(subs) > 0)

    def test_can_get_subscription(self):
        sub = self.service.get_subscription(self.subscription['id'])
        self.assertEqual(sub['id'], self.subscription['id'])

    def test_can_cancel_and_reactivate_subscription(self):
        self.assertEqual(self.subscription['status'], 'active')

        self.service.cancel_subscription(self.subscription['id'], 'testing')
        cancelled_sub = self.service.get_subscription(self.subscription['id'])
        self.assertEqual(cancelled_sub['status'], 'canceled')

        self.service.reactivate_subscription(cancelled_sub['id'], 'testing')
        reactivated_sub = self.service.get_subscription(cancelled_sub['id'])
        self.assertEqual(reactivated_sub['status'], 'active')
