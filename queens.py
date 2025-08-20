from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import logger
import re


class QueensBoard:
    rows: int
    cols: int
    cells: list()
    matrix: list()

    def __init__(self, grid):
        self.rows = int(grid.value_of_css_property('--rows'))
        self.cols = int(grid.value_of_css_property('--cols'))
        self.cells = grid.find_elements(
            By.CLASS_NAME, "queens-cell-with-border")
        self.matrix = [
            [None for _ in range(self.cols)] for _ in range(self.rows)]
        logger.debug("The game has been read")
        for cell in self.cells:
            hasQueen, color, row, col = self.extract_cell_info(cell)
            cell = Cell(color=color, row=row, col=col, hasQueen=hasQueen)
            self.matrix[row-1][col-1] = cell
        self.assign_neighbours()
        return

    def assign_neighbours(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.matrix[row][col]
                if cell is None:
                    continue
                neighbors = []
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            neighbor_cell = self.matrix[nr][nc]
                            if neighbor_cell is not None:
                                neighbors.append(neighbor_cell)
                cell.neighbors = neighbors

    def extract_cell_info(self, cell):
        pattern = r"(.+) of color (.+), row (\d+), column (\d+)"
        print("============================================")
        print(cell)
        print("============================================")
        text = cell.accessible_name
        print(text)
        match = re.fullmatch(pattern, text)
        hasQueen = True if (match.group(1) == "Queen") else False
        return (
            hasQueen,
            match.group(2),
            int(match.group(3)),
            int(match.group(4)))


class Solver:
    board: QueensBoard
    filled_row: list()
    filled_col: list()
    groups: dict()
    filled_color: list()

    def __init__(self, board: QueensBoard) -> None:
        self.board = board
        self.filled_col = []
        self.filled_row = []
        self.groups = {}
        self.filled_color = []

    def valid_square(self, cell: 'Cell') -> bool:
        if cell.row in self.filled_row:
            return False
        if cell.col in self.filled_col:
            return False
        for neighbour in cell.neighbors:
            if neighbour.hasQueen:
                return False
        return True

    def create_color_groups(self):
        # group cells into colours and store it in the dict
        # Later this will be used for iterating though the grid
        groups = {}
        for row in self.board.matrix:
            for cell in row:
                if cell is None:
                    continue
                color = cell.color
                if color not in groups:
                    groups[color] = []
                groups[color].append(cell)
        self.groups = groups
        return groups

    def solver(self):
        # Base case: if all colors are filled, solution is found
        if len(self.filled_color) == len(self.groups):
            return True

        # Find the next color group to fill
        for color in self.groups:
            if color not in self.filled_color:
                self.filled_color.append(color)
                for cell in self.groups[color]:
                    if self.valid_square(cell):
                        cell.hasQueen = True
                        self.filled_row.append(cell.row)
                        self.filled_col.append(cell.col)
                        if self.solver():
                            return True
                        # Backtrack
                        cell.hasQueen = False
                        self.filled_row.pop()
                        self.filled_col.pop()
                # Backtrack color group
                self.filled_color.pop()
                break
        return False

    def solve(self):
        self.create_color_groups()
        self.solver()


# CELL
class Cell:
    color: str
    row: int
    col: int
    hasQueen: bool
    neighbors: list()

    def __init__(self, color, row, col, hasQueen=False):
        self.color = color
        self.row = row - 1
        self.col = col - 1
        self.hasQueen = hasQueen
