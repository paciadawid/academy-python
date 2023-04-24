import requests


class APIHandler:
    base_url = "https://gorest.co.in/public/v2"
    user_endpoint = "/users"
    headers = {
        "Authorization": "Bearer 56c3f5739c2af4edb091c270360c0d22f7f804005a9b598801b24ee6b3e45f8f"
    }

    def create_user(self, body, expected_status_code=201):
        res = requests.post(self.base_url + self.user_endpoint, json=body, headers=self.headers)
        assert res.status_code == expected_status_code
        return res.json()

    def get_user_by_id(self, user_id, expected_status_code=200):
        res = requests.get(f"{self.base_url}{self.user_endpoint}/{user_id}", headers=self.headers)
        assert res.status_code == expected_status_code
        return res.json()

    def update_user(self, user_id, body):
        pass

    def delete_user(self, user_id):
        pass
