number_of_scrolls = 5


def find_element_with_scrolls(driver, selector, direction, scroll_size=0.5):
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

    for i in range(number_of_scrolls):
        driver.swipe(x_start, y_start, x_end, y_end)
        if driver.find_elements(*selector):
            return True
    return False
