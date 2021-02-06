from src.api.utils import ResultSerializer


class ComputeTemperature:
    """Class to compute temperature values."""

    def calculate_result(self, temperature_data):
        """Compute the average, min, max and median temperatures."""
        avg_list = [
            temp["day"]["avgtemp_f"]
            for temp in temperature_data["forecast"]["forecastday"]
        ]

        min_list = [
            temp["day"]["mintemp_f"]
            for temp in temperature_data["forecast"]["forecastday"]
        ]

        max_list = [
            temp["day"]["maxtemp_f"]
            for temp in temperature_data["forecast"]["forecastday"]
        ]

        median_list = sorted(avg_list)
        mid = len(avg_list) // 2

        result = {
            "maximum": round(max(max_list), 1),
            "minimum": round(min(min_list), 1),
            "average": round(sum(avg_list) / len(avg_list), 1),
            "median": round(
                ((median_list[mid] + median_list[~mid]) / 2), 1),

        }

        serializer = ResultSerializer(instance=result)

        return serializer.data
