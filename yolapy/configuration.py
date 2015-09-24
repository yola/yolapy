"""Configuration.

Yolapy.configuration provides a key-value store used by the Yola client.

Data is stored here in the module, benefits include:

 * Configuration is decoupled from application logic.

 * When instantiating multiple service models, each contains its own client.
   This module allows for configuration to happen once then consumed multiple
   times by each client.

See README for example of use.

"""
_config = {}
_default = object()


def configure(**kwargs):
    """Save all keyword arguments as (key=value) configuration."""
    _config.update(kwargs)


def get_config(key, default=_default):
    """Lookup the value of a configuration key using an optional default."""
    config = _config.get(key, default)
    if config == _default:
        raise KeyError('%s is not configured' % key)
    return config
