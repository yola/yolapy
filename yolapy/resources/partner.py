class PartnerResourceMixin(object):

    """Methods for managing Partner resources."""

    def create_partner(self, **attributes):
        """Create a partner.

        ```
        partner = service.create_partner(
            id='COMPANY_ID',
            name='Company Name',
            parent_partner_id='PARENT_ID',
            properties={'name': 'value'})
        partner['name'] # => 'Company Name'
        ```

        See <https://wl.qa.yola.net/partners/> for available properties.
        """
        return self.post(self._partner_path(), data=attributes).json()

    def get_partner(self, partner_id):
        """Return details for a particular partner.

        ```
        partner = service.get_partner('PARTNER_ID')
        partner['name'] # => 'Company Name'
        ```
        """
        return self.get(self._partner_path(partner_id)).json()

    def delete_partner(self, partner_id):
        """Delete a partner.

        `service.delete_partner('PARTNER_ID')`
        """
        self.delete(self._partner_path(partner_id))

    def update_partner(self, partner_id, **attributes):
        """Update a partner.

        `service.update_partner('PARTNER_ID', name='New name')`
        """
        return self.patch(
            self._partner_path(partner_id), data=attributes).json()

    def list_partners(self, **options):
        """Return paginated list of partners.

        `service.list_partners()`

        Example response:

        ```
        {
            'count': 999,
            'previous': None,
            'next': 'https://wl.qa.yola.net/pr/partners/?page=2',
            'results': [{...}, {...}, ...]
        }
        ```

        You can pass `page_size` and `page` as keyword arguments:

        `service.list_partners(page_size=50, page=2)`
        """
        return self.get(self._partner_path(), params=options).json()

    def _partner_path(self, *parts):
        path = '/'.join(['partners'] + list(parts))
        return '/%s/' % path
