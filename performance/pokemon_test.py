from locust import HttpUser, task, between

class PerfTest(HttpUser):

    host = "https://pokeapi.co/api/v2"
    wait_time = between(1, 2)

    @task
    def json_request(self):
        self.client.get("/pokemon-shape")

    @task
    def text_request(self):
        self.client.get("/pokemon?limit=100000")
