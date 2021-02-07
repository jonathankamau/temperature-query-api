"""API Viewsets."""
import json
import urllib
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from src.app.settings import WEATHER_API_KEY
from src.api.utils import ComputeTemperature


class TemperatureQuery(APIView):
    """Endpoint to query for temperature details."""

    def __init__(self):

        self.temperature_details = []
        self.compute = ComputeTemperature()

    def get(self, request, **kwargs):
        """
        Retrieve temperature data from weather API.

        return the min, max, average and median temperature data
        for that period.
        """
        city = kwargs.get('city')
        number_of_days = kwargs.get('number_of_days')
        response = None

        if not city.replace(" ", "").isalpha():
            response = Response(
                {
                    "Error":
                    f"{city} is invalid! Please provide a valid city name"
                },
                status=status.HTTP_400_BAD_REQUEST)

        elif not number_of_days.isnumeric():
            response = Response(
                {
                    'Error':
                    f"{number_of_days} is invalid! "
                    "Please provide a valid number for the days"
                },
                status=status.HTTP_400_BAD_REQUEST)

        elif int(number_of_days) < 1 or int(number_of_days) > 5:
            response = Response(
                {
                    "Error":
                    "Please provide a number_of_days value "
                    "within the range of 1 to 5"
                },
                status=status.HTTP_400_BAD_REQUEST)

        elif WEATHER_API_KEY is None:
            response = Response(
                {
                    "Error":
                    "Could not find the Weather API Key! "
                    "Ensure the Weather API Key is available."
                },
                status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                self.temperature_details = self.grab_weather_api_response(
                    city, number_of_days)

                result = self.compute.calculate_result(
                    self.temperature_details)

                response = Response(
                    result,
                    status=status.HTTP_200_OK
                )
            except urllib.error.HTTPError as e:
                if e.getcode() == 400:
                    response = Response(
                        {
                            "Error":
                            f"Could not get temperature details for {city}. "
                            f"Please provide a valid city name or check the "
                            f"name format and try again."
                        },
                        status=status.HTTP_400_BAD_REQUEST)
        return response

    def grab_weather_api_response(self, city, number_of_days):
        """Get the response for from the weather API."""
        weather_api_url = "https://api.weatherapi.com/v1/forecast.json"

        params = urllib.parse.urlencode(
            {
                "key": WEATHER_API_KEY,
                "q": city,
                "days": number_of_days
            }
        )

        url = f"{weather_api_url}?{params}"

        return json.load(urllib.request.urlopen(url))
