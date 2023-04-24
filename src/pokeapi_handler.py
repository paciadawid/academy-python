import requests


class APIHandler:
    base_url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = "/pokemon"
    shape_endpoint = "/pokemon-shape"

    def get_list_of_pokemons(self, params=None):
        res = requests.get(self.base_url + self.pokemon_endpoint, params=params)
        assert res.status_code == 200
        assert res.elapsed.microseconds / 1000 < 1000
        return res.json()

    def get_list_of_shapes(self):
        res = requests.get(self.base_url + self.shape_endpoint)
        assert res.status_code == 200
        return res.json()

    def get_shape_by_name(self, shape):
        res = requests.get(f"{self.base_url}{self.shape_endpoint}/{shape}")
        assert res.status_code == 200
        return res.json()
