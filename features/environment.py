import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.login import LoginPage


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.driver.implicitly_wait(10)
    context.driver.get("https://automationexercise.com/")
    context.login_page = LoginPage(context.driver)


def after_scenario(context, scenario):
    if scenario.status != "passed":
        # make screenshot
        allure.attach(context.driver.get_screenshot_as_png(), name="test.xyz",
                      attachment_type=allure.attachment_type.PNG)
    context.driver.quit()
