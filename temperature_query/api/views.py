"""API Viewsets."""
import json
import urllib
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from temperature_query.app.settings import WEATHER_API_KEY, WEATHER_API_URL
from temperature_query.api.utils import ComputeTemperature


class TemperatureQuery(APIView):
    """Endpoint to query for temperature details."""

    def __init__(self):

        self.temperature_details = []
        self.compute = ComputeTemperature()

    def get(self, request, city, number_of_days):
        """
        Retrieve temperature data from weather API.

        return the min, max, average and median temperature data
        for that period.
        """
        if not city.replace(" ", "").isalpha():
            return Response(
                {
                    "Error":
                    f"{city} is invalid! Please provide a valid city name"
                },
                status=status.HTTP_400_BAD_REQUEST)

        if not number_of_days.isnumeric():
            return Response(
                {
                    'Error':
                    f"{number_of_days} is invalid! "
                    "Please provide a valid number for the days"
                },
                status=status.HTTP_400_BAD_REQUEST)

        if WEATHER_API_KEY is None:
            return Response(
                {
                    'Error':
                    f"Could not find the Weather API Key! "
                    f"Ensure the Weather API Key is available."
                },
                status=status.HTTP_400_BAD_REQUEST)

        try:
            self.temperature_details = self.grab_weather_api_response(
                city, number_of_days)

        except urllib.error.HTTPError as e:
            if e.getcode() == 400:
                return Response(
                    {
                        "Error":
                        f"Could not get temperature details for {city}. "
                        f"Please provide a valid city name or check the "
                        f"name format and try again."
                    },
                    status=status.HTTP_400_BAD_REQUEST)

        if len(self.temperature_details) == 0:

            return Response(
                {
                    "Error":
                    f"Could not retrieve temperature data for {city}"
                },
                status=status.HTTP_404_NOT_FOUND)

        result = self.compute.calculate_result(self.temperature_details)
        return Response(
            result,
            status=status.HTTP_200_OK
        )

    def grab_weather_api_response(self, city, number_of_days):
        """Get the response for from the weather API."""
        params = urllib.parse.urlencode(
            {
                "key": WEATHER_API_KEY,
                "q": city,
                "days": number_of_days
            }
        )

        url = f"{WEATHER_API_URL}?{params}"

        return json.load(urllib.request.urlopen(url))
