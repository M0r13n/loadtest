import random
from locust import HttpUser, task, between
from requests.models import Response

APPLE_DEVICES = ("iPhone 7", "iPhone 6S", "iPhone X", "iPhone 8", "iPhone XS", "iPhone 8 Plus")
HUAWEI_DEVICES = ("P10", "P10 Lite", "P20 Lite", "P10 Plus", "P20 Pro")
SAMSUNG_DEVICES = ("S8", "S7", "S6", "S5", "S10 ", "S10 5G")
MANUFACTURERS = {
    "Huawei": ("P-Serie", HUAWEI_DEVICES),
    "Samsung": ("S-Serie", SAMSUNG_DEVICES),
    "Apple": ("iPhone", APPLE_DEVICES)
}


class UserWithoutCheckout(HttpUser):
    wait_time = between(5, 9)

    @task(3)
    def visit_main_page_task(self):
        self.client.get("/")

    @task(3)
    def visit_manufacturer_page_task(self):
        self.client.get("/manufacturer")

    @task
    def visit_manufacturer_page_task(self):
        manufacturer = random.choice(list(MANUFACTURERS.keys()))
        self.client.get(f"/{manufacturer}/series")

    def visit_series_list_page(self):
        manufacturer = random.choice(list(MANUFACTURERS.keys()))
        series = MANUFACTURERS[manufacturer][0]
        self.client.get(f"/{manufacturer}/{series}")

    @task
    def pick_device_task(self):
        manufacturer = random.choice(list(MANUFACTURERS.keys()))
        series = MANUFACTURERS[manufacturer][0]
        device = random.choice(MANUFACTURERS[manufacturer][1])
        self.client.get(f"/{manufacturer}/{series}/{device}")
