from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by  import By

def check_params(params):
    for key, value in params.items():
        print("{}\t:{}".format(key,value))

def scrape(params):
    """use to run the scraping script"""
    url = params['url']
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # insert_fields(driver)
    # driver.quit()
    return 0

def insert_fields(driver):
    negara = driver.find_element(By.CLASS_NAME('col-md-8 col-sm-12"')).click()
