"""API URLS file."""
from django.urls import path
from temperature_query.api.views import TemperatureQuery

get_temperature = TemperatureQuery.as_view({"get": "get_temperature"})

urlpatterns = [
    path(
        r"api/locations/<str:city>/days=<int:number_of_days>",
        get_temperature,
        name="temperature",
    )
]
