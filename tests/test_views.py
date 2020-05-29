"""Views test module."""
from django.test import TestCase

import django_sorting_bootstrap.views


class SimpleChangeListTests(TestCase):
    def test_create(self):
        django_sorting_bootstrap.views.SimpleChangeList(
            "request", "model", "list_display"
        )
