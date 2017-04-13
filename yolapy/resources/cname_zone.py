class CnameZoneMixin(object):
    """Methods for managing Cname Zones."""
    def create_cname_zone(self, hostname, partner_id):
        return self.post(
            self._cname_zones_path(),
            json={'partner_id': partner_id, 'hostname': hostname}).json()

    def _cname_zones_path(self, *parts):
        path = '/'.join(['cname-dns-zones'] + list(parts))
        return '/%s/' % path
