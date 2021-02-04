"""API Viewsets."""
import os
import json
import urllib
from rest_framework import viewsets, mixins
from rest_framework.response import Response


class TemperatureQuery(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Endpoint to query for temperature details."""

    def get_temperature(self, city, number_of_days):
        """Retrieve temperature data from weather API."""
        params = urllib.parse.urlencode(
            {"key": os.getenv("WEATHER_API_KEY"), "q": city,
             "days": number_of_days}
        )

        url = f"{os.getenv('WEATHER_API_URL')}?{params}"

        temperature_details = json.load(urllib.request.urlopen(url))

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
            }
        )
