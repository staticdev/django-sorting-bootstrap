Django Sorting Bootstrap
========================

**MAINTAINER NEEDED: this project is complete but won't be updated until further notice. If you have interest in improving it, please contact me by creating an** `issue here`_ **.**

|PyPI| |Python Version| |License|

|Read the Docs| |Tests|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/django-sorting-bootstrap.svg
   :target: https://pypi.org/project/django-sorting-bootstrap/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/django-sorting-bootstrap
   :target: https://pypi.org/project/django-sorting-bootstrap
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/django-sorting-bootstrap
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/django-sorting-bootstrap/latest.svg?label=Read%20the%20Docs
   :target: https://django-sorting-bootstrap.readthedocs.io/
   :alt: Read the documentation at https://django-sorting-bootstrap.readthedocs.io/
.. |Tests| image:: https://github.com/staticdev/django-sorting-bootstrap/workflows/Tests/badge.svg
   :target: https://github.com/staticdev/django-sorting-bootstrap/actions?workflow=Tests
   :alt: Tests
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

Django Sorting Bootstrap is a pluggable mini-API to easy add sorting for querysets, links and table headers in Django_ templates. There is also a new tag that creates headers for sorting tables using Bootstrap_'s layout.


Requirements
------------

* Python 3.7+
* Django 2.0+
* Bootstrap 3+


Installation
------------

You can install *Django Sorting Bootstrap* via pip_ from PyPI_:

.. code:: console

   $ pip install django-sorting-bootstrap


Documentation
-------------

Complete instructions on installation and usage are found in ``docs`` directory and online at
https://django-sorting-bootstrap.readthedocs.io.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the MIT_ license,
*Django Sorting Bootstrap* is free and open source software.


Credits
-------

This app is based on `Agiliq's django-sorting`_ 0.1. It has two improvements over it: the new tags and the Twitter Bootstrap compliance idea.


.. _issue here: https://github.com/staticdev/staticdev/issues
.. _Django: https://www.djangoproject.com/
.. _Bootstrap: http://getbootstrap.com/
.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _pip: https://pip.pypa.io/
.. _Agiliq's django-sorting: http://github.com/agiliq/django-sorting
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
