from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = "https://www.linkedin.com/"


def login(driver, url, username, password):
    driver.get(url)
    login_button = driver.find_element(By.XPATH, "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']")
    login_button.click()

    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("thipak01balaji@gmail.com")
    password_input.send_keys("specTra_01")

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and @data-litms-control-urn='login-submit']")
    submit_button.click()

def load_tango():
    driver.get("https://www.linkedin.com/games/tango/")
    time.sleep(10)


login(driver, url, "test@test.com", "test")
load_tango()

driver.quit()