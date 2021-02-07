"""Error Responses class module."""

from rest_framework.response import Response
from rest_framework import status


class ErrorResponses:
    """Class to register all the error responses."""

    def city_isnot_alpha(self, city):
        """Error to be returned if city provided isn't an alpha value."""
        return Response(
            {
                "Error":
                f"{city} is invalid! Please provide a valid city name"
            },
            status=status.HTTP_400_BAD_REQUEST)

    def days_not_numeric(self, number_of_days):
        """Error to be returned if day provided isn't a numeric value."""
        return Response(
                {
                    "Error":
                    f"{number_of_days} is invalid! "
                    "Please provide a valid number for the days"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def days_out_of_range(self, number_of_days):
        """Error to be returned if day provided is out of range."""
        return Response(
                {
                    "Error":
                    "Please provide a number_of_days value "
                    "within the range of 1 to 5"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def missing_weatherapi_key(self):
        """Error to be returned if the weather api key is missing."""
        return Response(
                {
                    "Error":
                    "Could not find the Weather API Key! "
                    "Ensure the Weather API Key is available."
                },
                status=status.HTTP_400_BAD_REQUEST)

    def weatherapi_error(self, city):
        """Error to be returned if request made to weatherapi is invalid."""
        return Response(
                {
                    "Error":
                    f"Could not get temperature details for {city}. "
                    f"Please provide a valid city name or check the "
                    f"name format and try again."
                },
                status=status.HTTP_400_BAD_REQUEST)
