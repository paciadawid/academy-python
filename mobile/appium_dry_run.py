import os
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
# Returns abs path relative to this file and not cwd
app_name = "nat.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps["automationName"] = "uiautomator2"

desired_caps['appPackage'] = "com.google.android.apps.maps"
desired_caps['appActivity'] = "com.google.android.maps.MapsActivity"
desired_caps['noReset'] = True
# desired_caps['app'] = app_path
# desired_caps['appPackage'] = "com.wdiodemoapp"
# desired_caps['appActivity'] = "com.wdiodemoapp.MainActivity"

driver = webdriver.Remote('http://localhost:4723', desired_caps)
driver.implicitly_wait(10)
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Drag").click()
# AndroidElement = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Carousel")
#driver.swipe(800, 1400, 400, 1400)

# el1 = driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='card'])[1]")
# el2 = driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='card'])[2]")
#
# driver.scroll(el2, el1)

# el1 = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='drag-l2']")
# el2 = driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='drop-l2']")
#
# driver.drag_and_drop(el1, el2)


xx = driver.get_window_size()['width']/2
yy = driver.get_window_size()['height']/2
# Zoom
# action1 = TouchAction(driver)
# action2 = TouchAction(driver)
#
# action1.long_press(x=xx, y=yy).move_to(x=0, y=200).wait(500).release()
# action2.long_press(x=xx, y=yy).move_to(x=0, y=-200).wait(500).release()
#
# m_action = MultiAction(driver)
# m_action.add(action1, action2)
#
# # Pinch
# action3 = TouchAction(driver)
# action4 = TouchAction(driver)
# action3.long_press(x=xx, y=yy-50).move_to(x=0, y=200).wait(500).release()
# action4.long_press(x=xx, y=yy+50).move_to(x=0, y=-200).wait(500).release()
#
# m_action2 = MultiAction(driver)
# m_action2.add(action3, action4)
#
# m_action.perform()
# m_action2.perform()


# json_wire = {
#     "actions": [[{
#                 "action": "longPress",
#                 "options": {
#                     "x": 540,
#                     "y": 986,
#                     "duration": 1000
#                 }
#             }, {
#                 "action": "moveTo",
#                 "options": {
#                     "x": 0,
#                     "y": 200,
#                     "ms": 20000
#                 }
#             }, {
#                 "action": "wait",
#                 "options": {
#                     "ms": 500
#                 }
#             }, {
#                 "action": "release",
#                 "options": {}
#             }
#         ], [{
#                 "action": "longPress",
#                 "options": {
#                     "x": 540,
#                     "y": 1086,
#                     "duration": 1000
#                 }
#             }, {
#                 "action": "moveTo",
#                 "options": {
#                     "x": 0,
#                     "y": -200,
#                     "ms": 20000
#                 }
#             }, {
#                 "action": "wait",
#                 "options": {
#                     "ms": 500
#                 }
#             }, {
#                 "action": "release",
#                 "options": {}
#             }
#         ]]
# }
#
# driver.execute("multiAction", json_wire)

