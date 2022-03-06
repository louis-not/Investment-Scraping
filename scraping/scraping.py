from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def check_params(params):
    for key, value in params.items():
        print("{}\t:{}".format(key,value))

def scrape(params):
    """use to run the scraping script"""
    url = params['url']
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3)
    try:
        insertion = insert_fields(driver, params)

        if insertion:
            print('process succeed')
    finally:
        time.sleep(5)
        driver.quit()

    return 0

def insert_fields(driver,params):
    """use to insert fields from the params to the website and request for data"""
    driver.find_element(By.XPATH,'/html/body/form/div/div/div/div/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div/a/span').click()
    driver.find_element(By.XPATH,'/html/body/form/div/div/div/div/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div/div/div/input').send_keys('Negara\n')
    driver.find_element(By.XPATH, '//*[@id="peringkat"]/table/tbody/tr[2]/td/div[1]/div[2]/div/label/span').click()
    driver.find_element(By.XPATH, '//*[@id="tahunAwal_chosen"]/a/span').click()
    driver.find_element(By.XPATH, '//*[@id="tahunAwal_chosen"]/div/div/input').send_keys(str(params['tahunAwal']) + '\n')
    driver.find_element(By.XPATH, '//*[@id="tahunAkhir_chosen"]/a/span').click()
    driver.find_element(By.XPATH, '//*[@id="tahunAkhir_chosen"]/div/div/input').send_keys(str(params['tahunAkhir']) + '\n')
    driver.find_element(By.XPATH, '//*[@id="filterNegara_chosen"]').click()
    driver.find_element(By.XPATH, '//*[@id="filterNegara_chosen"]/ul/li/input').send_keys(params['negara'] + '\n')
    driver.find_element(By.XPATH, '//*[@id="peringkat"]/table/tbody/tr[4]/td/div/button').click()

    return True