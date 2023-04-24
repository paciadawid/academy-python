import requests


class APIHandler:

    base_url = "https://gorest.co.in/public/v2"
    user_endpoint = "/users"
    headers = {
        "Authorization": "Bearer 56c3f5739c2af4edb091c270360c0d22f7f804005a9b598801b24ee6b3e45f8f"
    }

    def create_user(self, body):
        res = requests.post(self.base_url+self.user_endpoint, json=body, headers=self.headers)
        assert res.status_code == 201
        return res.json()