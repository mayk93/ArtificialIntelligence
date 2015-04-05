"""Holds secret data for calculating the csrf value.

`CSRF_KEY` must be set before using `CsrfField`.
"""
CSRF_KEY=None

class UnsetCsrfKeyError(Exception):
    pass