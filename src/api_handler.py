import requests


class APIHandler:
    base_url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = "/pokemon"

    def get_list_of_pokemons(self, params=None):
        res = requests.get(self.base_url + self.pokemon_endpoint, params=params)
        assert res.status_code == 200
        assert res.elapsed.microseconds / 1000 < 1000
        return res.json()
