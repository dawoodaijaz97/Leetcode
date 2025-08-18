class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.columns = 26
        self.grid = [[0] * self.columns for _ in range(self.rows)]

    def setCell(self, cell: str, value: int) -> None:
        col_index = ord(cell[0]) - ord('A')
        row_index = int(cell[1:]) - 1
        if 0 <= row_index < self.rows and 0 <= col_index < self.columns:
            self.grid[row_index][col_index] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        parts = formula[1:].split('+')
        total = 0
        for part in parts:
            if part.isdigit():
                total += int(part)
            else:
                col_index = ord(part[0]) - ord('A')
                row_index = int(part[1:]) - 1
                if 0 <= row_index < self.rows and 0 <= col_index < self.columns:
                    total += self.grid[row_index][col_index]
        return total

def solve(*args, **kwargs):
    # This function is a placeholder for the entry point.
    # It should be replaced with actual logic to handle input arguments
    # and call the appropriate methods of the Spreadsheet class.
    pass