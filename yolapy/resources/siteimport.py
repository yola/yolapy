class SiteImportResourceMixin(object):
    _path = '/pr/jobs/sites/'

    def create_site_import(self, **data):
        return self.post(
            self._path, json=data).json()

    def get_site_import(self, id):
        return self.get('{url}{id}/'.format(url=self._path, id=id)).json()

    def list_site_imports(self, **options):
        return self.get(self._path, params=options).json()
