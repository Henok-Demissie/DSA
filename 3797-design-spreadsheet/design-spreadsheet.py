class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        parts = formula[1:].split('+')
        return sum(int(p) if p.isdigit() else self.cells.get(p, 0) for p in parts)