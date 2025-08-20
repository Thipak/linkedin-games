from selenium import webdriver
from selenium.webdriver.common.by import By
from auth import login
from queens import QueensBoard, Solver


driver = webdriver.Firefox()

# LOGIN
login(driver)
# Queens Game get input
game = QueensBoard(grid=driver.find_element(By.ID, "queens-grid"))

solver = Solver(game)
solver.solve()
print(solver.board)
for i in range(game.rows):
    for j in range(game.cols):
        print(game.matrix[i][j].hasQueen, end=" ")
    print()

# Queens Game End
driver.quit()
