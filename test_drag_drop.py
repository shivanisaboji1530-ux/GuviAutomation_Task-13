import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# Positive Test Case
def test_drag_and_drop_positive(driver):

    driver.get("https://jqueryui.com/droppable/")

    # Switch to iframe
    frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "demo-frame"))
    )
    driver.switch_to.frame(frame)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    ActionChains(driver).drag_and_drop(source, target).perform()

    assert target.text == "Dropped!"
    driver.save_screenshot("reports/drag_and_drop_positive.png")


# Negative Test Case
def test_drag_and_drop_negative(driver):

    driver.get("https://jqueryui.com/droppable/")

    frame = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(frame)

    target = driver.find_element(By.ID, "droppable")

    # Intentionally incorrect validation
    assert target.text != "Dropped!"

    driver.save_screenshot("reports/drag_and_drop_negative.png")