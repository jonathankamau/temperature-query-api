"""Base test module."""

from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    """Base test class."""

    def setUp(self):
        """Contains common mock test utilities."""
        self.city = "London"
        self.number_of_days = 3

        self.response = self.client.get(
            f"/api/locations/{self.city}/days={self.number_of_days}",
            format="application/json")

        self.fake_temp_data = {
            "location": {
                "name": "London",
                "region": "City of London, Greater London",
                "country": "United Kingdom",
                "lat": 51.52,
                "lon": -0.11,
                "tz_id": "Europe/London",
                "localtime_epoch": 1612558416,
                "localtime": "2021-02-05 20:53"
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2021-02-05",
                        "date_epoch": 1612483200,
                        "day": {
                            "maxtemp_c": 10.6,
                            "maxtemp_f": 51.1,
                            "mintemp_c": 5.6,
                            "mintemp_f": 42.1,
                            "avgtemp_c": 7.7,
                            "avgtemp_f": 45.9,
                            "maxwind_mph": 7.8,
                            "maxwind_kph": 12.6,
                            "totalprecip_mm": 0,
                            "totalprecip_in": 0,
                            "avgvis_km": 6.8,
                            "avgvis_miles": 4,
                            "avghumidity": 86,
                            "daily_will_it_rain": 0,
                            "daily_chance_of_rain": "0",
                            "daily_will_it_snow": 0,
                            "daily_chance_of_snow": "0",
                            "condition": {
                                "text": "Partly cloudy",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                "code": 1003
                            },
                            "uv": 1
                        },
                        "astro": {
                            "sunrise": "07:32 AM",
                            "sunset": "04:58 PM",
                            "moonrise": "01:39 AM",
                            "moonset": "11:01 AM",
                            "moon_phase": "Waning Crescent",
                            "moon_illumination": "34"
                        },
                    },
                    {
                        "date": "2021-02-06",
                        "date_epoch": 1612569600,
                        "day": {
                            "maxtemp_c": 6.8,
                            "maxtemp_f": 44.2,
                            "mintemp_c": 5.4,
                            "mintemp_f": 41.7,
                            "avgtemp_c": 6,
                            "avgtemp_f": 42.8,
                            "maxwind_mph": 14.1,
                            "maxwind_kph": 22.7,
                            "totalprecip_mm": 18.7,
                            "totalprecip_in": 0.74,
                            "avgvis_km": 7.6,
                            "avgvis_miles": 4,
                            "avghumidity": 90,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": "92",
                            "daily_will_it_snow": 0,
                            "daily_chance_of_snow": "0",
                            "condition": {
                                "text": "Moderate rain",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/302.png",
                                "code": 1189
                            },
                            "uv": 1
                        },
                        "astro": {
                            "sunrise": "07:31 AM",
                            "sunset": "04:59 PM",
                            "moonrise": "03:01 AM",
                            "moonset": "11:31 AM",
                            "moon_phase": "Waning Crescent",
                            "moon_illumination": "28"
                        },
                    },
                    {
                        "date": "2021-02-07",
                        "date_epoch": 1612656000,
                        "day": {
                            "maxtemp_c": 0.6,
                            "maxtemp_f": 33.1,
                            "mintemp_c": -1.5,
                            "mintemp_f": 29.3,
                            "avgtemp_c": 0.3,
                            "avgtemp_f": 32.6,
                            "maxwind_mph": 16.6,
                            "maxwind_kph": 26.6,
                            "totalprecip_mm": 11.3,
                            "totalprecip_in": 0.44,
                            "avgvis_km": 3.1,
                            "avgvis_miles": 1,
                            "avghumidity": 83,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": "88",
                            "daily_will_it_snow": 1,
                            "daily_chance_of_snow": "73",
                            "condition": {
                                "text": "Heavy snow",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/338.png",
                                "code": 1225
                            },
                            "uv": 1
                        },
                        "astro": {
                            "sunrise": "07:29 AM",
                            "sunset": "05:01 PM",
                            "moonrise": "04:20 AM",
                            "moonset": "12:10 PM",
                            "moon_phase": "Waning Crescent",
                            "moon_illumination": "21"
                        },
                    },
                    {
                        "date": "2021-02-08",
                        "date_epoch": 1612656000,
                        "day": {
                            "maxtemp_c": 0.6,
                            "maxtemp_f": 33.1,
                            "mintemp_c": -1.5,
                            "mintemp_f": 29.3,
                            "avgtemp_c": 0.3,
                            "avgtemp_f": 32.6,
                            "maxwind_mph": 16.6,
                            "maxwind_kph": 26.6,
                            "totalprecip_mm": 11.3,
                            "totalprecip_in": 0.44,
                            "avgvis_km": 3.1,
                            "avgvis_miles": 1,
                            "avghumidity": 83,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": "88",
                            "daily_will_it_snow": 1,
                            "daily_chance_of_snow": "73",
                            "condition": {
                                "text": "Heavy snow",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/338.png",
                                "code": 1225
                            },
                            "uv": 1
                        },
                        "astro": {
                            "sunrise": "07:29 AM",
                            "sunset": "05:01 PM",
                            "moonrise": "04:20 AM",
                            "moonset": "12:10 PM",
                            "moon_phase": "Waning Crescent",
                            "moon_illumination": "21"
                        },
                    },
                    {
                        "date": "2021-02-09",
                        "date_epoch": 1612656000,
                        "day": {
                            "maxtemp_c": 0.6,
                            "maxtemp_f": 33.1,
                            "mintemp_c": -1.5,
                            "mintemp_f": 29.3,
                            "avgtemp_c": 0.3,
                            "avgtemp_f": 32.6,
                            "maxwind_mph": 16.6,
                            "maxwind_kph": 26.6,
                            "totalprecip_mm": 11.3,
                            "totalprecip_in": 0.44,
                            "avgvis_km": 3.1,
                            "avgvis_miles": 1,
                            "avghumidity": 83,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": "88",
                            "daily_will_it_snow": 1,
                            "daily_chance_of_snow": "73",
                            "condition": {
                                "text": "Heavy snow",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/338.png",
                                "code": 1225
                            },
                            "uv": 1
                        },
                        "astro": {
                            "sunrise": "07:29 AM",
                            "sunset": "05:01 PM",
                            "moonrise": "04:20 AM",
                            "moonset": "12:10 PM",
                            "moon_phase": "Waning Crescent",
                            "moon_illumination": "21"
                        },
                    }

                ]
            }
        }
