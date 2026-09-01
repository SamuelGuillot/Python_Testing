from locust import HttpUser, task, between

class GUDLFTPerfTest(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.email = "perfa@test.com"
        self.club_name = "Perf Club A"
        self.client.post("/showSummary", data={"email": self.email})

    @task(1)
    def afficher_accueil(self):
        self.client.post("/showSummary", data={"email": self.email})

    @task(2)
    def consulter_points(self):
        self.client.get("/points")

    @task(5)
    def reserver_places(self):
        self.client.post("/purchasePlaces", data={
            "club": self.club_name,
            "competition": "Perf Comp 1",
            "places": "2"
        })

    @task(1)
    def reserver_invalide(self):
        self.client.post("/purchasePlaces", data={
            "club": self.club_name,
            "competition": "Perf Comp 1",
            "places": "100000"
        })