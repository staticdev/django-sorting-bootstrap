Change-log for django-sorting-bootstrap.

Version 1.1 (2015/09/01)
==========================

- Changed raise statement to work with Python 3
- Adds support for Django < 1.5
- Better modularization. Thanks to caioariede.
- Fix on to use request.path instead of ./ when possible. Thanks to caioariede.
- Fixed rst2html.py (docutils 0.8 - for compliance with PyPI) warnings in README.rst.
- Reoganized README.rst for better understanding.

Version 1.0.2 (2013/15/09)
==========================

- Bug-fix in autosort for ChangeList usage

Version 1.0.1 (2013/15/09)
==========================

- Bug-fix in sort_headers current_sort_field comparison
- No use of Python reserved word sorted (now is is_sorted)
- Optimization in has_visible_name - it was taken off for better working
