Django Sorting Bootstrap
========================

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


Configuration
-------------

Include `django_sorting_bootstrap` in your `INSTALLED_APPS`

Put `{% load sorting_tags %}` at top of your templates.

Your templates have four tags available:

- `auto_sort`
- `sort_link`
- `sort_th`
- `sort_headers`


Usage
-----

.. code:: html

   {% auto_sort queryset %}
   {% sort_link "link text" "field_name" %}
   {% sort_th "link text" "field_name" %}
   {% sort_headers simpleschangelist %}


Django views
~~~~~~~~~~~~

For sorting to work, your views have to

1. add the current sort field to the context
2. apply the sorting to the queryset

For a generic ListView, this could be done as follows::

  from django.views.generic import ListView


  class ExampleListView(ListView):
      model = MyModel

      def get_context_data(self, **kwargs):
          # add current sort field to context
          c = super(ExampleListView, self).get_context_data(**kwargs)
          if "sort_by" in self.request.GET:
              c["current_sort_field"] = self.request.GET.get("sort_by")
          return c

      def get_queryset(self):
          # apply sorting
          qs = super(ExampleListView, self).get_queryset()
          if "sort_by" in self.request.GET:
              qs = qs.order_by(self.request.GET.get("sort_by"))
          return qs


Template Tags
~~~~~~~~~~~~~

1. auto_sort

It sorts the queryset in place and replaces the queryset by the sorted queryset.

This needs to be called prior to a slice has been taken from a queryset.
(Ordering can not be done after the slice has been taken.) In particular this will
not work with generuc view `object_list`.

Basic usage:

.. code:: html

   {% auto_sort queryset %}


2. sort_link

Sort link outputs a link which will sort on the given field. The field to sort on should be
a database field, or something which `.order_by` of queryset would work.

Basic usage:

.. code:: html

   {% sort_link "link text" "field_name" %}


Example usage:

.. code:: html

   {% sort_link "Name" "name" %}


It may also be used as:

.. code:: html

   {% sort_link "link text" "field_name" "vis_name" %} {% sort_link "Name" "name" "what" %}


This is useful if you do not wnat to expose your database fields in urls.

3. sort_th

It works the same way as sort_link, but the difference is the output template that renders a table header tag `<th>` using `Bootstrap`* classes and Glyphicons.

Basic usage:

.. code:: html

   {% sort_th "link text" "field_name" %}


4. sort_headers

This function is somewhat more complicated to use, but it builds the whole table headers for sorting. In order to use it you have to pass in your view a SimplesChangeList (from sorting_bootstrap.views).
Let's have an exemple using a view extending Generic ListView::

  from django.views.generic import ListView
  from sorting_bootstrap.views import SimpleChangeList


  class MyView(ListView)

      def get_context_data(self, **kwargs):
          # Calls the base implementation first to get a context
          context = super(self.__class__, self).get_context_data(**kwargs)
          # Gets the fields that are going to be in the headers
          list_display = [i.name for i in self.model._meta.fields]
          # Doesnt show ID field
          list_display = list_display[1:]
          cl = SimpleChangeList(self.request, self.model, list_display)
          # Pass a change list to the views
          context['cl'] = cl
          return context


You also need to call the function in your template:

.. code:: html

   <thead>
     <tr>
       {% sort_headers cl %}
     </tr>
   </thead>


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


.. _Django: https://www.djangoproject.com/
.. _Bootstrap: http://getbootstrap.com/
.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _pip: https://pip.pypa.io/
.. _Agiliq's django-sorting: http://github.com/agiliq/django-sorting
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
