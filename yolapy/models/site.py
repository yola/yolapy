from yolapy.services import Yola


class Site(object):
    """Represents a Site resource on the Yola API."""

    def __init__(self, **kwargs):
        for key, val in kwargs.iteritems():
            setattr(self, key, val)

    @classmethod
    def get(cls, site_id):
        site_attributes = Yola().get_site(site_id)
        return Site(**site_attributes)
