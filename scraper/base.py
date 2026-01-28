from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def get_driver() -> webdriver.Chrome:
    options = Options()

    #disable GPU hardware accel
    options.add_argument("--disable-gpu")
    #full HD resolution
    options.add_argument("--window-size=1920,1080")
    #reduces basic bot detection 
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    #mimic windows chrome browser
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )

    # Create the driver
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)

    return driver

def wait_for_element(driver: webdriver.Chrome, css_selector: str, timeout: int = 10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

def human_sleep(min_sec: float = 0.5, max_sec: float = 2.5):
    time.sleep(random.uniform(min_sec, max_sec))

def scroll_down(driver, pixels=500):
    driver.execute_script(f"window.scrollBy(0, {pixels});")
    human_sleep(0.5, 1.0)
