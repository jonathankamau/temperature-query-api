"""Temperature calculations testcases."""
from temperature_query.tests.base_test import BaseTestCase
from temperature_query.api.views import TemperatureQuery


class TempCalculations(BaseTestCase):
    """Test cases for  calculations."""

    def setUp(self):
        """Utilities for the tempCalculations class."""
        BaseTestCase.setUp(self)

        self.temp_query = TemperatureQuery()

    def test_average_temperature(self):
        """Test for average temperature."""
        expected_result = 37.3

        self.assertEqual(
            self.temp_query.average_temperature(self.mock_temp_data),
            expected_result
            )

    def test_min_temperature(self):
        """Test for minimum temperature."""
        expected_result = 29.3

        self.assertEqual(
            self.temp_query.min_temperature(self.mock_temp_data),
            expected_result
        )

    def test_max_temperature(self):
        """Test for maximum temperature."""
        expected_result = 51.1

        self.assertEqual(
            self.temp_query.max_temperature(self.mock_temp_data),
            expected_result
        )

    # def test_median_temperature(self):
    #     """Test for median temperature."""
    #     expected_result = 90

    #     self.assertEqual(
    #         self.temp_query.median_temperature(),
    #         expected_result
    #     )
