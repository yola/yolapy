from yolapy.services import Yola


class Site(object):
    """Represents a Site resource on the Yola API."""

    def __init__(self, **kwargs):
        self.publishing_data = kwargs.pop('publishing_data', {})
        for key, val in kwargs.iteritems():
            setattr(self, key, val)

    @classmethod
    def get(cls, site_id):
        """Get a site from the Yola API."""
        site_attributes = Yola().get_site(site_id)
        return Site(**site_attributes)

    @property
    def published_domain(self):
        return self.publishing_data.get('canonical_host')
