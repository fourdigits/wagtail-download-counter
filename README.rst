.. image:: https://travis-ci.org/fourdigits/wagtail-download-counter.svg?branch=master
    :target: https://travis-ci.org/fourdigits/wagtail-download-counter
    :alt: Build status


========================
Wagtail Download Counter
========================

Wagtail Download Counter is an add-on for `Wagtail CMS <https://github.com/torchbox/wagtail>`_ that keeps track of the number of times a document has been downloaded and shows the count in the Wagtail admin interface.

Usage
=====

In your settings file add the following:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'downloadcounter',
        ...
    ]

Make sure you add ``downloadcounter`` before ``wagtail.wagtaildocs`` in the installed apps.

Run migrations and you're set.
