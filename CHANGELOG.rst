0.8.0
------------------
* Remove calculating `Site.is_published` property,
  because it's already in api.

0.7.0
------------------
* Add `Yola.set_site_url` method.

0.6.2
------------------
* Run tests using maintained python versions : 2.7, 3.5, 3.6, 3.7, 3.8
* Add `Yola.complete_wl_task(wl_task_id)`
* Add `Yola.fail_wl_task(wl_task_id, reason)`

0.6.1
------------------
* Add `Yola.get_user_wsites` method.

0.6.0
------------------
* Remove `six` dependency
* Remove `User.save` method
* Add `User.create` classmethod
* Add `Yola.get_sso_url` method
* Fix bug caused by improper call signature to `create_site_import` method on
  `Yola` service
* Update `User.__init__` to accept `**kwargs` rather than named arguments. This
  makes it consistent with other yolapy models and more flexible in case of
  changes to data returned by the service.


0.5.0
------------------
* Remove `Yola.subscribe_to_campaign()` and `Yola.cancel_campaign_subscription`
  methods, they aren't allowed to be used externally.
* Add SiteImport model and api for creation and listing
* `Yola.get_sso_create_site_url` and `Yola.get_sso_open_site_url`
  now accept optional `locale` arguments which define what language the
  returned urls should be generated for


0.4.2
------------------
* Remove `with_ssl_support` flag for methods
  `User.get_sso_create_site_url()` and `Site.change_site_domain()`.
* Add `Yola.create_cname_zone()` method.


0.4.1
------------------
* Add support of `with_ssl_support` flag for methods
  `User.get_sso_create_site_url()` and `Site.change_site_domain()`.

0.4.0
------------------
* Update Subscription model to expect the actual data from service response.

0.3.0
------------------
* Drop support for python 3.2
* `Yola.get_sso_open_site_url` now accepts an optional `site_id` specifying the
  site to generate a url for
* Use Demands >= 4.0.0

0.2.4 (2016-06-17)
------------------
* Fix mismatch between demands version in setup.py and requirements.txt

0.2.3 (2016-06-17)
------------------

* Handle pagination in Site.list
* Add ``User.get`` class method that returns a populated User object

0.2.2 (2016-04-06)
------------------

* Add ``Site.is_published``

0.2.1 (2016-03-31)
------------------

* Add ``Site.list``

0.2.0 (2016-03-29)
------------------

* ``Yola.create_subscription`` now returns the created subscription.
* **Breaking change:** Remove ``Yola.suspend_user`` and ``Yola.resume_user``.
* Add a ``Site`` model.

0.1.7 (2015-12-02)
------------------

* Update Subscription model to include all attributes returned from the API.

0.1.6 (2015-12-01)
------------------

* Update installation requirements (demands)
* Support Python 3


0.1.5 (2015-11-23)
------------------

* Return values from ``change_subscription_type`` and ``activate_trial_subscription``
  methods.
* Fixed failing integration tests.


0.1.4 (2015-11-19)
------------------

* Add Subscription model

0.1.3 (2015-10-19)
------------------

* Add a Partner model


0.1.2 (2015-10-15)
------------------

* Add a configuration module
* Add a User model
* Add Sphinx Docs - http://yolapy.readthedocs.org/


0.1.1 (2015-09-11)
------------------

* Update installation requirements


0.1.0 (2015-09-02)
------------------

* Initial version with ``Yola`` wrapper for the Yola API
