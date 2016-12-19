from yolapy.services import Yola


class Subscription(object):

    """Construct a Subscription.

    :param auto_renew: Bool
    :param billing_date: Datetime
    :param deprovision_date: Datetime
    :param expiry_date: Datetime
    :param start_date: Datetime
    :param status: Str, subscription status
    :param term: Str, subscription billing term
    :param id: Str, subscription's 32 char ID
    :param properties: Dict, subscription properties. If unset will be
        defaulted to the client's configured username:
        ``{"partner_id": "<CLIENT_USERNAME>"}``.
    :param sku: Int
    :param type: Str, subscription type
    :param user_id: Str, 32 character ID of the sub's user

    :return: Subscription
    :rtype: yolapy.models.Subscription

    """

    _fields = (
        'id', 'created_at', 'updated_at', 'partner_id', 'user_id', 'status',
        'term', 'sku', 'type', 'start_date', 'expiry_date', 'billing_date',
        'deprovision_date', 'auto_renew', 'properties')

    def __init__(self, **fields):
        self.client = Yola()
        for field_name in self._fields:
            setattr(self, field_name, fields[field_name])

    @classmethod
    def list(cls, **kwargs):
        """Return a filtered list of Subscriptions.

        Usage::

           >>> from yolapy.models import Subscription
           >>> user_id = 'abcdef1234567890abcdef1234567890'
           >>> user_subs = Subscription.list(user_id=user_id)
           >>> print user_subs[0]
           <yolapy.models.subscription.Subscription object>
           >>> print user_subs[0].user_id
           u'abcdef1234567890abcdef1234567890'
        """
        response = Yola().list_subscriptions(**kwargs)
        return [cls(**sub) for sub in response['results']]
