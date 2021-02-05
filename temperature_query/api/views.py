"""API Viewsets."""
import os
import json
import urllib
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class TemperatureQuery(APIView):
    """Endpoint to query for temperature details."""

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
                    "Please provide a valid digit for the number of days"
                },
                status=status.HTTP_400_BAD_REQUEST)

        params = urllib.parse.urlencode(
            {
                "key": os.getenv("WEATHER_API_KEY"),
                "q": city,
                "days": number_of_days
            }
        )

        url = f"{os.getenv('WEATHER_API_URL')}?{params}"

        temperature_details = []
        try:
            temperature_details = json.load(urllib.request.urlopen(url))
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

        if len(temperature_details) == 0:

            return Response(
                {
                    "Error":
                    f"Could not retrieve temperature data for {city}"
                },
                status=status.HTTP_404_NOT_FOUND)

        min_list = [
            temp["day"]["mintemp_f"]
            for temp in temperature_details["forecast"]["forecastday"]
        ]
        max_list = [
            temp["day"]["maxtemp_f"]
            for temp in temperature_details["forecast"]["forecastday"]
        ]
        avg_list = [
            temp["day"]["avgtemp_f"]
            for temp in temperature_details["forecast"]["forecastday"]
        ]
        median_list = sorted(avg_list)
        mid = len(avg_list) // 2

        return Response(
            {
                "maximum": max(max_list),
                "minimum": min(min_list),
                "average": sum(avg_list) / len(avg_list),
                "median": (median_list[mid] + median_list[~mid]) / 2,
            },
            status=status.HTTP_200_OK
        )
