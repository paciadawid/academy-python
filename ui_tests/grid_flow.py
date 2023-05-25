from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("window-size=1000,800")
options.add_argument("--headless")

driver = webdriver.Remote("http://192.168.1.28:4444", options=options)

driver.get("https://automationexercise.com/")
sleep(10)
driver.quit()
