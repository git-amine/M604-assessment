import unittest
from src.data_preprocessing.countries import country_to_continent

class TestCountryToContinent(unittest.TestCase):
    def test_country_to_continent(self):
        # Test cases for randomly chosen countries
        test_cases = {
            "Canada": "North America",
            "Brazil": "South America",
            "Germany": "Europe",
            "Nigeria": "Africa",
            "Japan": "Asia",
            "Yemen, Rep.": "Asia",
            "Yemen": "Asia",
            "Congo, Rep.": "Africa",
            "Congo": "Africa",
            "Australia": "Oceania",

        }

        for country, expected_continent in test_cases.items():
            with self.subTest(country=country):
                result = country_to_continent(country)
                self.assertEqual(result, expected_continent, f"Failed for {country}")


if __name__ == "__main__":
    unittest.main()

