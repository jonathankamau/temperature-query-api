"""
Tests module for the API.

- Tests for the endpoint.
- Tests for related methods.
"""

from rest_framework.test import APITestCase
from rest_framework import status


class BaseTestCase(APITestCase):
    """Base test class."""

    pass


class QueryEndpointTestcase(BaseTestCase):
    """Testcases for the API endpoint."""

    def setUp(self):
        """Contains mock data for tests."""
        self.correct_response_keys = [
            "maximum", "minimum", "average", "median"
            ]

    def test_get_temperature_data(self):
        """Tests the temperature query endpoint for correct response."""
        city = "London"
        number_of_days = 3

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            self.correct_response_keys, list(response.data.keys())
            )
