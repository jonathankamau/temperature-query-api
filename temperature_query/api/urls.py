"""API URLS file."""
from django.conf.urls import url
from temperature_query.api.views import TemperatureQuery

urlpatterns = [
    url(
        r"locations/(?P<city>\w+)/days=(?P<number_of_days>\w+)/$",
        TemperatureQuery.as_view(),
        name="temperature",
    )
]
