from locust import HttpUser, TaskSet, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_all(self):
        self.client.get("/get")
        
    @task
    def get_by_id(self):
        self.client.get("/get_by_identifier")
        
    @task
    def get_by_lastname(self):
        self.client.get("/get_by_lastname")
        
    @task
    def get_by_country(self):
        self.client.get("/get_by_country")
