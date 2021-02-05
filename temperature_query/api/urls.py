"""API URLS file."""
from django.urls import re_path
from temperature_query.api.views import TemperatureQuery

urlpatterns = [
    re_path(
        r"locations/(?P<city>[\w\s\w]+)/days=(?P<number_of_days>\w+)$",
        TemperatureQuery.as_view(),
        name="temperature",
    )
]
