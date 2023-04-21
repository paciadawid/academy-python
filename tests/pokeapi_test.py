import unittest

import requests

from src.api_handler import APIHandler


class PokeAPITests(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()

    def test_default_list_of_pokemons(self):
        res_json = self.api_handler.get_list_of_pokemons()
        self.assertEqual(1281, res_json["count"])

        # self.assertLess(int(res.headers["content-length"]), 100 * 1000)
        # self.assertLess(len(res.content), 100 * 1000)
        # end_time = time.time()
        # print(end_time-start_time)

    def test_pokemon_list_with_pagination(self):
        params = {
            "limit": 10,
            "offset": 20
        }

        res_json = self.api_handler.get_list_of_pokemons(params)
        self.assertEqual(params["limit"], len(res_json["results"]))
        self.assertRegex(res_json["results"][0]["url"], f".*\/{params['offset'] + 1}\/.*")  # 1

        # url = res_json["results"][0]["url"]
        # id = url.split("/")[-2]
        # self.assertEqual(str(first_id), id)  # 2
        # self.assertIn(str(first_id), res_json["results"][0]["url"])  # 3

    def test_shapes_and_ids(self):
        res_json = self.api_handler.get_list_of_shapes()
        self.assertEqual(res_json["count"], len(res_json["results"]))
        third_shape = res_json["results"][2]["name"]
        res_json = self.api_handler.get_shape_by_name(third_shape)
        self.assertEqual(3, res_json["id"])


if __name__ == '__main__':
    unittest.main()
