import unittest

import requests

import time

class PokeAPITests(unittest.TestCase):

    base_url = "https://pokeapi.co/api/v2/pokemon"

    def test_default_list_of_pokemons(self):
        #start_time = time.time()
        res = requests.get(self.base_url)
        res_json = res.json()
        self.assertTrue(res_json)
        self.assertEqual(200, res.status_code)
        self.assertEqual(1281, res_json["count"])
        self.assertLess(1000, res.elapsed.microseconds/1000)
        self.assertLess(100 * 1000, res.headers["content-length"])
        self.assertLess(100 * 1000, len(res.content))

        #end_time = time.time()
        #print(end_time-start_time)



if __name__ == '__main__':
    unittest.main()
