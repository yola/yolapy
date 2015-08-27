from demands import HTTPServiceClient

from yolapy.resources.partner import PartnerResourceMixin
from yolapy.resources.site import SiteResourceMixin
from yolapy.resources.user import UserResourceMixin


class Yola(
        HTTPServiceClient, PartnerResourceMixin, SiteResourceMixin,
        UserResourceMixin):

    """Client for Yola's API.

    ```
    service = Yola(
        url='https://wl.yola.net/',
        auth=('username', 'password'))

    service.get_user('user_id')
    ```

    When appropriate, successful responses will return parsed json objects.

    Failures will raise instances of `demands.HTTPServiceError`.

    See [TODO] for available methods with documentation.
    """

    def __init__(self, **kwargs):
        """Initialize with url, auth, and optional headers.

        ```
        Yola(
            url='https://wl.yola.net/',
            auth=('username', 'password'),
            headers={'Header-Name': 'value'})
        ```
        """
        kwargs['send_as_json'] = True
        super(Yola, self).__init__(**kwargs)
