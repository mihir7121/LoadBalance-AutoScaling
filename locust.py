from locust import HttpUser, task

class loadgen(HttpUser):
    @task
    def load(self):
        self.client.get("/fibonacci")
        self.client.get("/fibonacci?n=27")