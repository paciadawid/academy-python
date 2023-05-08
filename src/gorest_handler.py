import requests
from faker import Faker


class APIHandler:
    base_url = "https://gorest.co.in/public/v2"
    user_endpoint = "/users"
    post_endpoint = "/posts"
    headers = {
        "Authorization": "Bearer 56c3f5739c2af4edb091c270360c0d22f7f804005a9b598801b24ee6b3e45f8f"
    }

    def create_user(self, body=None, expected_status_code=201, random_user=False):
        if random_user:
            body = {
                "name": Faker().name(),
                "gender": "male",
                "email": Faker().email(),
                "status": "active"
            }
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

    def create_post(self, user_id, post_body, expected_status_code=201):
        res = requests.post(f"{self.base_url}{self.user_endpoint}/{user_id}{self.post_endpoint}", json=post_body, headers=self.headers)
        assert res.status_code == expected_status_code
        return res.json()

    def get_post(self, post_id, expected_status_code=200):
        res = requests.get(f"{self.base_url}{self.post_endpoint}/{post_id}", headers=self.headers)
        assert res.status_code == expected_status_code
        return res.json()

    def delete_post(self, post_id):
        res = requests.delete(f"{self.base_url}{self.post_endpoint}/{post_id}", headers=self.headers)
        assert res.status_code == 204
