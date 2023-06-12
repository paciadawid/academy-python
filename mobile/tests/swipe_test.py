import os

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

app_name = "gestures.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['app'] = app_path
desired_caps["automationName"] = "uiautomator2"

desired_caps["appPackage"] = "com.wdiodemoapp"
desired_caps["appActivity"] = "com.wdiodemoapp.MainActivity"

driver = webdriver.Remote('http://localhost:4723', desired_caps)

# north_pin = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "North up view")
# x = north_pin.location["x"]
# y = north_pin.location["y"]
#
# driver.swipe(x - 1, y, 1, y, 3000)
