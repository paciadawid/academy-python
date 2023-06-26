from locust import HttpUser, task, between



class PerfTest(HttpUser):

    host = "https://api.ipify.org"
    wait_time = between(1, 2)

    @task(3)
    def json_request(self):
        self.client.get("/?format=json")

    @task(1)
    def text_request(self):
        self.client.get("/?format=text")
