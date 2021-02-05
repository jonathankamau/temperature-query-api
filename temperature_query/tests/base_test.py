"""Base test module."""

from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    """Base test class."""

    def setUp(self):
        """Contains common mock test utilities."""
        pass
