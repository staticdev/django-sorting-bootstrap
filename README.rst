django-sorting-bootstrap
========================

.. image:: https://pypip.in/v/django-sorting-bootstrap/badge.png
        :target: https://pypi.python.org/pypi/django-sorting-bootstrap

Django-sorting-bootstrap is a pluggable mini-API to easy add sorting for querysets, links and table headers in Django_ templates. There is also a new tag that creates headers for sorting tables using `Bootstrap`_'s layout.

Installation
------------
To install ``django-sorting-bootstrap`` simply run::

    pip install django-sorting-bootstrap

Configuration
-------------

Include `sorting_bootstrap` in your `INSTALLED_APPS`

Put `{% load sorting_tags %}` at top of your templates.

Your templates have four tags available:

`auto_sort`
`sort_link`
`sort_th`
`sort_headers`

Basic usage::

    {% auto_sort queryset %}
    {% sort_link "link text" "field_name" %}
    {% sort_th "link text" "field_name" %}
    {% sort_headers simpleschangelist %}
    

auto_sort
-------------------
It sorts the queryset in place and replaces the queryset by the sorted queryset.

This needs to be called prior to a slice has been taken from a queryset.
(Ordering can not be done after the slice has been taken.) In particular this will
not work with generuc view `object_list`.

Basic usage::

    {% auto_sort queryset %}


sort_link
-----------------
Sort link outputs a link which will sort on the given field. The field to sort on should be
a database field, or something which `.order_by` of queryset would work.

Basic usage::

    {% sort_link "link text" "field_name" %}

Example usage::
    
    {% sort_link "Name" "name" %}
    
It may also be used as::
    
    {% sort_link "link text" "field_name" "vis_name" %}
    {% sort_link "Name" "name" "what" %}
    
This is useful if you do not wnat to expose your database fields in urls.


sort_th
-------------------
It works the same way as sort_link, but the difference is the output template that renders a table header tag <th> using `Bootstrap`_ classes and Glyphicons.

Basic usage::

    {% sort_th "link text" "field_name" %}


sort_headers
-------------------
This function is somewhat more complicated to use, but it builds the whole table headers for sorting. In order to use it you have to pass in your view a SimplesChangeList (from sorting_bootstrap.views).
Let's have an exemple using a view extending Generic ListView.

Basic usage::

    from django.views.generic import ListView
    class MyView(ListView)
      def get_context_data(self, **kwargs):
                # Calls the base implementation first to get a context
            context = super(self.__class__, self).get_context_data(**kwargs)
            
            from sorting_bootstrap.views import SimpleChangeList
            # Gets the fields that are going to be in the headers
            list_display = [i.name for i in self.model._meta.fields]
            # Doesnt show ID field
            list_display = list_display[1:]
            cl = SimpleChangeList(self.request, self.model, list_display)
            # Pass a change list to the views
            context['cl'] = cl

You also need to call the function in your template::

    <thead>
    <tr>
    {% sort_headers cl %}
    </tr>
    </thead>


Credits
------------

This app is based on Agiliq's `django-sorting`_ 0.1. It has two improvements over it: the new tags and the Twitter Bootstrap compliance idea.

.. _Django: https://www.djangoproject.com/
.. _Bootstrap: http://getbootstrap.com/
.. _django-sorting: http://github.com/agiliq/django-sorting
