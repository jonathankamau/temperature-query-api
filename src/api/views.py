"""API Viewsets."""
import urllib
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from src.app.settings import WEATHER_API_KEY
from src.api.utils import (ComputeTemperature, ErrorResponses,
                           grab_weather_api_response)


class TemperatureQuery(APIView):
    """Endpoint to query for temperature details."""

    def __init__(self):
        """Initialize variables."""
        self.temperature_details = []
        self.compute = ComputeTemperature()
        self.error_response = ErrorResponses()

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

            response = self.error_response.city_isnot_alpha(city)

        elif not number_of_days.isnumeric():
            response = self.error_response.days_not_numeric(
                number_of_days)

        elif int(number_of_days) < 1 or int(number_of_days) > 5:
            response = self.error_response.days_out_of_range(
                number_of_days)

        elif WEATHER_API_KEY is None:
            response = self.error_response.missing_weatherapi_key()

        else:
            try:
                self.temperature_details = grab_weather_api_response(
                    WEATHER_API_KEY, city, number_of_days)

                result = self.compute.calculate_result(
                    self.temperature_details)

                response = Response(
                    result,
                    status=status.HTTP_200_OK
                )
            except urllib.error.HTTPError as e:
                if e.getcode() == 400 or e.getcode() == 404:
                    response = self.error_response.weatherapi_error(city)

        return response
