class SiteResourceMixin(object):

    """Methods for managing Site resources."""

    def list_sites(self, **options):
        """Return paginated list of sites.

        `service.list_sites()`

        Example response:

        ```
        {
            'count': 999,
            'previous': None,
            'next': 'https://wl.qa.yola.net/pr/sites/?page=2',
            'results': [{...}, {...}, ...]
        }
        ```

        You can pass `page_size` and `page` as keyword arguments:

        `service.list_sites(page_size=50, page=2)`

        You can also pass filters and odering options as keyword arguments.
        See <https://wl.qa.yola.net/sites/> for available options.
        """
        return self.get(self._site_path(), params=options).json()

    def get_site(self, site_id):
        """Return details for a particular site.

        ```
        site = service.get_site('site_id')
        site['name'] # => 'My Site'
        ```
        """
        return self.get(self._site_path(site_id)).json()

    def disable_site(self, site_id):
        """Disable a site.

        `service.disable_site('site_id')`
        """
        self.post(self._site_path(site_id, 'disable'))

    def enable_site(self, site_id):
        """Enable a site.

        `service.enable_site('site_id')`
        """
        self.post(self._site_path(site_id, 'enable'))

    def change_site_owner(self, site_id, new_user_id):
        """Change site owner.

        `service.change_site_owner('site_id', 'new_user_id')`
        """
        data = {'id': new_user_id}
        self.post(self._site_path(site_id, 'change_owner'), data=data)

    def change_partner_domain(self, site_id, new_domain):
        """Change site's partner domain.

        `service.change_site_partner_domain('site_id', 'newdomain.com')`
        """
        data = {'partner_domain': new_domain}
        self.put(self._site_path(site_id, 'partner_domain'), data=data)

    def delete_site(self, site_id):
        """Delete a site.

        ```
        service.get_site('site_id')['deleted_at'] # => None
        service.delete_site('site_id')
        service.get_site('site_id')['deleted_at'] # => timestamp
        ```
        """
        self.delete(self._site_path(site_id))

    def undelete_site(self, site_id):
        """Un-delete a site.

        ```
        service.get_site('site_id')['deleted_at'] # => timestamp
        service.delete_site('site_id')
        service.get_site('site_id')['deleted_at'] # => None
        ```
        """
        self.post(self._site_path(site_id, 'undelete'))

    def _site_path(self, *parts):
        path = '/'.join(['sites'] + list(parts))
        return '/%s/' % path
