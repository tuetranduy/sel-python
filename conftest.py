import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://www.w3schools.com/python/python_tuples.asp"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
