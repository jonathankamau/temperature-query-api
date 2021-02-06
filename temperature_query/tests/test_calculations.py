"""Temperature calculations testcases."""
from temperature_query.tests.base_test import BaseTestCase
from temperature_query.api.utils import ComputeTemperature


class TempCalculations(BaseTestCase):
    """Test cases for temperature calculations."""

    def setUp(self):
        """Utilities for the tempCalculations class."""
        BaseTestCase.setUp(self)

        self.temp_query = ComputeTemperature()

        self.result = self.temp_query.calculate_result(
            self.fake_temp_data)

    def test_average_temperature(self):
        """Test for average temperature."""
        self.assertEqual(
            self.result["average"], 37.3)

    def test_min_temperature(self):
        """Test for minimum temperature."""
        self.assertEqual(
            self.result["minimum"], 29.3)

    def test_max_temperature(self):
        """Test for maximum temperature."""
        self.assertEqual(
            self.result["maximum"], 51.1)

    def test_median_temperature(self):
        """Test for median temperature."""
        self.assertEqual(
            self.result["median"], 32.6)
