from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

def check_params(params):
    for key, value in params.items():
        print("{}\t:{}".format(key,value))

def scrape(params):
    """use to run the scraping script"""
    url = params['url']
    # for chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)

    try:
        selector = '//select[@id="berdasarkan"]'
        element = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
        element.click()
        # wait = WebDriverWait(driver,10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, selector))).click()
        # driver.find_element(By.XPATH, selector).click()

    # insert_fields('//*[@id="berdasarkan"]',)
    finally:
        driver.quit()

    return 0

def insert_fields(xPath):

    negara = driver.find_element(By.CLASS_NAME('col-md-8 col-sm-12"')).click()
