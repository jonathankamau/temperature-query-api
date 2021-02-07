"""Grab the response given from the Public Weatheapi."""
import json
import urllib


def grab_weather_api_response(WEATHER_API_KEY, city, number_of_days):
    """Get the response from the weather API."""
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
