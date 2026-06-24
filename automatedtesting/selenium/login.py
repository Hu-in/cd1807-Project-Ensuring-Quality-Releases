from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def login(user, password):
    print("Starting Firefox...")

    options = Options()

    # ✅ nutzt geckodriver im selben Ordner
    service = Service("./geckodriver.exe")

    driver = webdriver.Firefox(
        service=service,
        options=options
    )

    print("Opening website...")
    driver.get("https://www.saucedemo.com")

    time.sleep(5)

    input("Press ENTER to close browser...")

login("standard_user", "secret_sauce")
