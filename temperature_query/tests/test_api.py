"""Tests module for the API.

- Tests for the endpoint.
- Tests for related methods.
"""
from unittest.mock import patch
from rest_framework import status

from temperature_query.tests.base_test import BaseTestCase


class QueryEndpointTestcase(BaseTestCase):
    """Testcases for the API endpoint."""

    def test_get_temperature_data(self):
        """Tests the temperature query endpoint for correct response."""
        correct_response_keys = [
            "maximum", "minimum", "average", "median"
            ]

        city = "London"
        number_of_days = 3

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            correct_response_keys, list(response.data.keys())
            )

    def test_invalid_city_name(self):
        """Test the response given if the city name is invalid."""
        city = "87454_939"
        number_of_days = 1

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
                    "Error":
                    f"{city} is invalid! Please provide a valid city name"
                }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data, expected_message)

    def test_invalid_days(self):
        """Test the response received if the day value is invalid."""
        city = "New York"
        number_of_days = "Mark"

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
                    'Error':
                    f"{number_of_days} is invalid! "
                    "Please provide a valid number for the days"
                }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data, expected_message)

    def test_inability_get_temperature_data(self):
        """
        Test the response if unable to get data for city from weather API.
        """
        city = "bloomwashington"
        number_of_days = 2

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
                        "Error":
                        f"Could not get temperature details for {city}. "
                        f"Please provide a valid city name or check the "
                        f"name format and try again."
                }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data, expected_message)

    @patch("temperature_query.api.views.WEATHER_API_KEY", None)
    def test_weather_api_key_not_available(self):

        city = "London"
        number_of_days = 3

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
                    'Error':
                    f"Could not find the Weather API Key! "
                    f"Ensure the Weather API Key is available."
                }

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data, expected_message)
