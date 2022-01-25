from locust import HttpUser, task, between
from faker import Faker

fake = Faker()


class ExampleUser(HttpUser):
    #wait_time = between(1, 3)

    @task(1)
    def get_all_examples(self):
        with self.client.get("/api/v1/examples/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("No data")

    @task(1)
    def create_example(self):
        with self.client.post(
            "/api/v1/examples/",
            json={"name": fake.name(), "description": fake.job()},
            catch_response=True,
        ) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure("No data")