from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://automationexercise.com/")

# searching element
driver.find_element(By.CLASS_NAME, "logo")
# cart - not possible to find
driver.find_element(By.ID, "susbscribe_email")
# banner switch - not possible to find
# brands - not possible to find
driver.find_element(By.ID, "footer")

# css selectors
driver.find_elements(By.CSS_SELECTOR, ".logo")
driver.find_element(By.CSS_SELECTOR, "li [href='/view_cart']")
driver.find_element(By.CSS_SELECTOR, "#susbscribe_email")
driver.find_element(By.CSS_SELECTOR, ".control-carousel.right")
driver.find_element(By.CSS_SELECTOR, ".brands_products>h2")
driver.find_element(By.CSS_SELECTOR, "#footer")

# xpath selectors
driver.find_element(By.XPATH, '//*[@class="logo pull-left"]')
driver.find_element(By.XPATH, '//li/a[@href="/view_cart"]')
driver.find_element(By.XPATH, '//input[@id="susbscribe_email"]')
driver.find_element(By.XPATH, '//div[@id="slider-carousel"]//i[@class="fa fa-angle-right"]')
driver.find_element(By.XPATH, '//div[@class="brands_products"]/h2')
driver.find_element(By.XPATH, '//footer[@id="footer"]')


driver.quit()
