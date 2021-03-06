from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


def check_params(params):
    for key, value in params.items():
        print("{}\t:{}".format(key, value))


def scrape(params):
    """use to run the scraping script"""
    url = params['url']
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
    driver.get(url)
    time.sleep(1)
    insertion = insert_fields(driver, params)
    time.sleep(5)
    pmdn, pma = get_data(driver)

    if insertion and pmdn is not None and pma is not None:
        print('scraping process succeed')

    # time.sleep(2)
    # driver.quit()

    return pmdn, pma


def insert_fields(driver, params):
    """use to insert fields from the params to the website and request for data"""
    try:
        driver.find_element(By.XPATH,
                            '/html/body/form/div/div/div/div/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div/a/span'
                            ).click()
        driver.find_element(By.XPATH,
                            '/html/body/form/div/div/div/div/table/tbody/tr[1]/td/div/div[2]/div[1]/div/div/div/div/input'
                            ).send_keys(params['field']+'\n')
        driver.find_element(By.XPATH,
                            '//*[@id="peringkat"]/table/tbody/tr[2]/td/div[1]/div[2]/div/label/span'
                            ).click()
        driver.find_element(By.XPATH,
                            '//*[@id="tahunAwal_chosen"]/a/span'
                            ).click()
        driver.find_element(By.XPATH,
                            '//*[@id="tahunAwal_chosen"]/div/div/input'
                            ).send_keys(str(params['tahunAwal']) + '\n')
        driver.find_element(By.XPATH,
                            '//*[@id="tahunAkhir_chosen"]/a/span'
                            ).click()
        driver.find_element(By.XPATH,
                            '//*[@id="tahunAkhir_chosen"]/div/div/input'
                            ).send_keys(str(params['tahunAkhir']) + '\n')
        # driver.find_element(By.XPATH,
        #                     '//*[@id="filterNegara_chosen"]'
        #                     ).click()
        # driver.find_element(By.XPATH,
        #                     '//*[@id="filterNegara_chosen"]/ul/li/input'
        #                     ).send_keys(params['negara'] + '\n')
        driver.find_element(By.XPATH,
                            '//*[@id="filterProv_chosen"]'
                            ).click()
        driver.find_element(By.XPATH,
                            '//*[@id="filterProv_chosen"]/ul/li/input'
                            ).send_keys(params['provinsi'] + '\n')
        driver.find_element(By.XPATH,
                            '//*[@id="peringkat"]/table/tbody/tr[4]/td/div/button'
                            ).click()
    except Exception:
        print('insert_fields failed')
        return False
    finally:
        return True


def get_data(driver):
    """scrape data from intended page"""
    try:
        selector_pmdn = '#rt_NS_ > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td:nth-child(3) > table'
        table_pmdn = driver.find_element(By.CSS_SELECTOR, selector_pmdn).get_attribute("outerHTML")
        pmdn = pd.read_html(table_pmdn, header=0)
        selector_pma = '#rt_NS_ > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td:nth-child(1) > table'
        table_pma = driver.find_element(By.CSS_SELECTOR, selector_pma).get_attribute("outerHTML")
        pma = pd.read_html(table_pma, header=0)
        return pmdn, pma

    except Exception:
        print('Failed getting data from table')
        # try:
        #     log = driver.find_element(By.XPATH,
        #                               '/html/body/form[1]/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[3]/div/span'
        #                               ).text
        #     if log == 'No data available':
        #         print('No data found')
        # finally:
        #     print('error on get_data function')
        return None
