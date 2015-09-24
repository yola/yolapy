from demands import HTTPServiceClient
from yolapy.configuration import get_config
from yolapy.resources import campaign, partner, site, subscription, user


class Yola(
        HTTPServiceClient, campaign.CampaignResourceMixin,
        partner.PartnerResourceMixin, site.SiteResourceMixin,
        subscription.SubscriptionResourceMixin, user.UserResourceMixin):
    """Client for Yola's API.

    If using yolapy.configuration:
    ```
    configure(yola={
        'url': 'https://wl.yola.net/',
        'auth': ('username', 'password')),
    })
    yola = Yola()
    yola.get_user('user_id')
    ```

    Or configured manually:
    ```
    yola = Yola(
        url='https://wl.yola.net/',
        auth=('username', 'password'))
    yola.get_user('user_id')
    ```

    When appropriate, successful responses will return parsed json objects.

    Failures will raise instances of `demands.HTTPServiceError`.

    See [TODO] for available methods with documentation.
    """

    def __init__(self, **kwargs):
        """Initialize with optional headers.

        Auth and url are expected to be present in the 'yola' configuration.

        Passed arguments will override configuration.

        ```
        Yola(headers={'Header-Name': 'value'})
        ```
        """
        config = {'send_as_json': True}
        config.update(get_config('yola', {}))
        config.update(kwargs)
        assert(config['url'])
        assert(config['auth'])
        super(Yola, self).__init__(**config)
