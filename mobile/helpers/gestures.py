import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_element_with_scrolls(driver, selector, direction, scroll_size=0.5, timeout=40):
    # scroll size - percentage of screen size
    window_size = driver.get_window_size()
    width = window_size["width"]
    height = window_size["height"]

    if direction == "UP":
        x_start = width / 2
        y_start = height * (1 - scroll_size / 2)
        x_end = width / 2
        y_end = height * (scroll_size / 2)
    elif direction == "LEFT":
        x_start = width * (1 - scroll_size / 2)
        y_start = height / 2
        x_end = width * (scroll_size / 2)
        y_end = height / 2

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            WebDriverWait(driver,0.1).until(EC.visibility_of_element_located(selector))
            return True
        except TimeoutException:
            driver.swipe(x_start, y_start, x_end, y_end)
    return False
