Yola API Python Client
======================

Usage
-----

.. code:: python

    # settings file

    from yolapy.configuration import configure

    configure(
        auth=('username', 'password'),
        url='https://wl.qa.yola.net/',
    )

    # application code

    from yolapy.models import User as YolaUser

    yola_user = YolaUser(
        email='test@example.com',
        name='Jane',
        surname='Doe',
        partner_id='WL_YOLA',
        preferences={'name': 'value'})
    yola_user.save()

See http://yolapy.readthedocs.org/ for available methods with
documentation.

Development
-----------

To run the tests::

    $ nosetests

Integration tests are not run by default. To run them, you must set up an
integration environment and edit the test settings::

    $ cp tests/test_integration/test_settings.py.sample \
    $    tests/test_integration/test_settings.py

Yola devs can get test auth credentials using the instructions on
[this wiki page][service-dev-wiki].

Then run them explicitly::

    $ nosetests tests/test_integration

To test and lint your code automatically when you make changes::

    $ cp tube.py.sample tube.py
    $ stir

Documentation
-------------

Changes to the public interface should be documented. See the `docs` directory.

Pushes to the `master` branch build at http://yolapy.readthedocs.org/en/latest/
automatically.

You can test your doc changes locally with::

    $ cd docs
    $ make html
    $ open _build/html/index.html


[service-dev-wiki]: https://github.com/yola/wiki/wiki/Service-and-Client-guidelines#development
