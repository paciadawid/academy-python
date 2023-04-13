import unittest
import requests


class TestPunkAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "https://api.punkapi.com/v2/beers"

    def test_default_beers(self):
        res_body = requests.get(self.base_url).json()
        self.assertEqual(1, res_body[0]["id"])
        self.assertEqual(25, len(res_body))

    def test_beer_123(self):
        requests.get(self.base_url + "/123")

    def test_40_element_4th_page(self):
        params = {
            "page": 4,
            "per_page": 40
        }
        requests.get(self.base_url, params=params)

    def test_ids_1_to_5(self):
        params = {
            "ids": "1|2|3|4|5"
        }
        requests.get(self.base_url, params=params)

    def test_abv_5_to_7(self):
        params = {
            "abv_gt": 4.9,
            "abv_lt": 7.1
        }
        requests.get(self.base_url, params=params)

    def test_brewed_in_2010(self):
        params = {
            "brewed_before": "01-2011",
            "brewed_after": "12-2009"
        }
        requests.get(self.base_url, params=params)


if __name__ == '__main__':
    unittest.main()
