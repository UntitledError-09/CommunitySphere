# locustfile.py
# locust configuration file
from locust import HttpUser, task, between


class CommunitySphereUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def visit_home_page(self):
        self.client.get("/")
