from demands.pagination import PaginatedResults
from six import iteritems

from yolapy.services import Yola


class SiteImport(object):
    def __init__(self, **kwargs):
        for key, val in iteritems(kwargs):
            setattr(self, key, val)

    @classmethod
    def create(cls, url, user_id):
        return cls(**Yola().create_site_import(url, user_id))

    @classmethod
    def get(cls, id):
        return cls(**Yola().get_site_import(id))

    @classmethod
    def list(cls, **filters):
        site_imports = PaginatedResults(
            Yola().list_site_imports, kwargs=filters)
        return [cls(**site_import) for site_import in site_imports]
