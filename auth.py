from selenium.webdriver.common.by import By

# CONSTANTS
LINKEDIN_URL = "https://www.linkedin.com/"
QUEENS_URL = LINKEDIN_URL + "games/queens/"
EMAIL = "thipak01balaji@gmail.com"
PASSWORD = "specTra_01"


# login
def login(driver):
    # Go to Login Page
    driver.get(LINKEDIN_URL)
    login_button = driver.find_element(By.XPATH, "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']")
    login_button.click()

    # Enter Credentials and submit
    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)

    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and @data-litms-control-urn='login-submit']")
    submit_button.click()

    # Redirect to Queens
    driver.get(QUEENS_URL)
