# Yola API Python Client

## Usage

```python
from yolapy.services import Yola


yola = Yola(
    url='https://wl.qa.yola.net/',
    auth=('username', 'password'))

yola.create_user(
    email='test@example.com',
    name='Jane',
    surname='Doe',
    partner_id='WL_YOLA',
    preferences={'name='value'})
```

See <http://yolapy.readthedocs.org/en/latest/> for available methods with
documentation.
