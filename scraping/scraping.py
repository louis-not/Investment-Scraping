from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = r'C:\Users\fxnic\Documents\ChromeDriver\chromedriver.exe'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://nswi.bkpm.go.id/data_statistik")

print(driver.page_source)
# driver.quit()