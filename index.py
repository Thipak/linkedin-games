from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

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

def load_queens():
    driver.get("https://www.linkedin.com/games/queens/")

class Cell():
    color: str
    row: int
    col: int
    hasQueen: bool

    def __init__(self, color, row, col, hasQueen=False):
        self.color = color
        self.row = row - 1
        self.col = col - 1
        self.hasQueen = hasQueen

def extract_cell_info(cell):
    pattern = r"(.+) of color (.+), row (\d+), column (\d+)"
    print("===========================================================================")
    print(cell)
    print("===========================================================================")
    text = cell.accessible_name
    print(text)
    match = re.fullmatch(pattern, text)
    hasQueen = True if(match.group(1) == "Queen") else False
    return (hasQueen, match.group(2), int(match.group(3)), int(match.group(4)))




def read_game():
    grid = driver.find_element(By.ID, "queens-grid")
    number_of_rows = int(grid.value_of_css_property('--rows'))
    number_of_columns = int(grid.value_of_css_property('--cols'))
    print(number_of_rows," ---- ")
    print(number_of_columns, "++++++++++")
    cells = grid.find_elements(By.CLASS_NAME, "queens-cell-with-border")
    assert len(cells) > 1
    print(len(cells))
    matrix = [[None for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    for i in cells:
        hasQueen, color, row, col = extract_cell_info(i)
        cell = Cell(color=color, row=row, col=col, hasQueen=hasQueen)
        matrix[row-1][col-1] = cell

    print(matrix)

    pass



login(driver, url, "test@test.com", "test")

# Queens Game
load_queens()
# Queens Game get input
read_game()


# Queens Game End

driver.quit()