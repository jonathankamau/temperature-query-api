from src.api.utils import ResultSerializer
from collections import defaultdict


class ComputeTemperature:
    """Class to compute temperature values."""

    def calculate_result(self, temperature_data):
        """Compute the average, min, max and median temperatures."""
        temp_values = defaultdict(list)

        for day in temperature_data["forecast"]["forecastday"]:

            temp_values['avg_list'].append(day["day"]["avgtemp_f"])
            temp_values['min_list'].append(day["day"]["mintemp_f"])
            temp_values['max_list'].append(day["day"]["maxtemp_f"])

        median_list = sorted(temp_values['avg_list'])
        mid = len(temp_values['avg_list']) // 2

        result = {
            "maximum": round(max(temp_values['max_list']), 1),
            "minimum": round(min(temp_values['min_list']), 1),
            "average": round(sum(temp_values['avg_list']) /
                             len(temp_values['avg_list']), 1),
            "median": round(
                ((median_list[mid] + median_list[~mid]) / 2), 1),

        }

        serializer = ResultSerializer(instance=result)

        return serializer.data
