from locust import HttpLocust, TaskSet, task
from random import randint

class UserBehavior(TaskSet):
    
    @task
    def sum_operation(self):
        response = self.client.get("/")
        print("Response status code:", response.status_code)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 500