========================
Wagtail Download Counter
========================

Wagtail Download Counter is an add-on for `Wagtail CMS <https://github.com/torchbox/wagtail>` that keeps track of the number of times a document has been downloaded and shows the coutn in the Wagtail admin interface.

Usage
=====

In your settings file add the following:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'downloadcounter',
        ...
    ]

Make sure you add ``downloadcounter`` before ``wagtal.wagtaildocs`` in the installed apps.

Run migrations and you're set.
