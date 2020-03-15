# django-sorting-bootstrap

|pyversions| |Travis| |PyPi|

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/django-sorting-bootstrap.svg
    :target: https://pypi.python.org/pypi/django-sorting-bootstrap
    :alt: Python versions supported

.. |Travis| image:: https://api.travis-ci.org/staticdev/django-sorting-bootstrap.svg?branch=master
.. _Travis: https://travis-ci.org/staticdev/django-sorting-bootstrap

.. |PyPi| image:: https://badge.fury.io/py/django-sorting-bootstrap.svg
.. _PyPi: https://badge.fury.io/py/django-sorting-bootstrap

Django-sorting-bootstrap is a pluggable mini-API to easy add sorting for querysets, links and table headers in [Django](https://www.djangoproject.com/) templates. There is also a new tag that creates headers for sorting tables using [Bootstrap](http://getbootstrap.com/)'s layout.

## Installation

To install `django-sorting-bootstrap` simply run:

```sh
pip install django-sorting-bootstrap
```

## Configuration

Include ``sorting_bootstrap`` in your ``INSTALLED_APPS``

Put ``{% load sorting_tags %}`` at top of your templates.

Your templates have four tags available:

* ``auto_sort``
* ``sort_link``
* ``sort_th``
* ``sort_headers``

## Basic usage

```html
{% auto_sort queryset %}
{% sort_link "link text" "field_name" %}
{% sort_th "link text" "field_name" %}
{% sort_headers simpleschangelist %}
```

## Django views

For sorting to work, your views have to

1. add the current sort field to the context
2. apply the sorting to the queryset

For a generic ListView, this could be done as follows::

```python
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
                qs = qs.order_by(self.request.GET.get("sort_by")
            return qs
```

## Template Tags

### auto_sort

It sorts the queryset in place and replaces the queryset by the sorted queryset.

This needs to be called prior to a slice has been taken from a queryset.
(Ordering can not be done after the slice has been taken.) In particular this will
not work with generuc view `object_list`.

Basic usage:

```html
{% auto_sort queryset %}
```

## sort_link

Sort link outputs a link which will sort on the given field. The field to sort on should be
a database field, or something which `.order_by` of queryset would work.

Basic usage:

```html
{% sort_link "link text" "field_name" %}
```

Example usage:

```html
{% sort_link "Name" "name" %}
```

It may also be used as:

```html
{% sort_link "link text" "field_name" "vis_name" %}
{% sort_link "Name" "name" "what" %}
```

This is useful if you do not wnat to expose your database fields in urls.

## sort_th

It works the same way as sort_link, but the difference is the output template that renders a table header tag `<th>` using `Bootstrap`_ classes and Glyphicons.

Basic usage:

```html
{% sort_th "link text" "field_name" %}
```

## sort_headers

This function is somewhat more complicated to use, but it builds the whole table headers for sorting. In order to use it you have to pass in your view a SimplesChangeList (from sorting_bootstrap.views).
Let's have an exemple using a view extending Generic ListView.

```python
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
```

You also need to call the function in your template:

```html
<thead>
    <tr>
    {% sort_headers cl %}
    </tr>
</thead>
```

## Credits

This app is based on [Agiliq's django-sorting](http://github.com/agiliq/django-sorting) 0.1. It has two improvements over it: the new tags and the Twitter Bootstrap compliance idea.
