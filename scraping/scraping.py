from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by  import By

def open_url(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    print(driver.page_source)
    insert_fields(driver)
    # driver.quit()
    return 0

def insert_fields(driver):
    negara = driver.find_element(By.CLASS_NAME('col-md-8 col-sm-12"')).click()

if __name__ == '__main__':
    open_url("https://nswi.bkpm.go.id/data_statistik")