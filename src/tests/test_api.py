"""Tests module for the API.

- Tests for the endpoint.
- Tests for related methods.
"""
import importlib
from unittest.mock import patch
from rest_framework import status
import src.app.settings

from src.tests.base_test import BaseTestCase

importlib.reload(src.app.settings)


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

    @patch("src.api.views.WEATHER_API_KEY", None)
    def test_weather_api_key_not_available(self):
        """Test for when the weather API key isn't provided."""
        city = "London"
        number_of_days = 3

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
                    "Error": "Could not find the Weather API Key! "
                    "Ensure the Weather API Key is available."
                }

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data, expected_message)

    def test_days_less_than_one(self):
        """Test if the number of days provided is less than 1."""

        city = "London"
        number_of_days = 0

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
            "Error":
            "Please provide a number_of_days value within the range of 1 to 5"
                }

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data, expected_message)

    def test_days_greater_than_five(self):
        """Test if number of days is greater than 5."""

        city = "London"
        number_of_days = 32

        response = self.client.get(
            f"/api/locations/{city}/days={number_of_days}",
            format="application/json")

        expected_message = {
                    "Error":
                    "Please provide a number_of_days value "
                    "within the range of 1 to 5"
                }

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data, expected_message)

    @patch.dict(
        "os.environ",
        {
            "ENVIRONMENT": "docker-development",
            "HOST": "0.0.0.0"
        })
    def test_docker_allowed_hosts(self):
        """Test if the docker host environment variable is in allowed hosts."""
        importlib.reload(src.app.settings)
        self.assertEqual(
            src.app.settings.ALLOWED_HOSTS, ["0.0.0.0"]
        )
