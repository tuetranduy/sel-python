from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverManager:
    driver = None

    def create_driver(self):
        options = webdriver.ChromeOptions()
        print("in create_webdriver")

        self.driver = webdriver.Chrome(service=Service(), options=options)