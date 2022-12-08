from dataclasses import dataclass, field


@dataclass
class Tree():
    height: int
    visible: bool = False


@dataclass
class Forest():
    _grid: list[list[Tree]] = field(default_factory=lambda: [[]])

    def __init__(self, x_size: int, y_size: int) -> None:

        self._grid = [[None for _ in range(y_size)] for _ in range(x_size)]

    def fill_row(self, row_id: int, row_data: str):
        for index, height in zip(range(len(row_data)), row_data):
            self._grid[row_id][index] = Tree(height=int(height))

    def fill_forest(self, rows: list[str]):
        for index, row_data, in zip(range(len(rows)), rows):
            self.fill_row(index, row_data.strip())

    def check_visibility(self):
        for row in self._grid:
            self.set_line_visibility(row)
            self.set_line_visibility(row[::-1])
        for index in range(len(self._grid)):
            col = [row[index] for row in self._grid]
            self.set_line_visibility(col)
            self.set_line_visibility(col[::-1])

    def set_line_visibility(self, line: list[Tree]):
        max_height = -1
        for item in line:
            if item.height > max_height:
                item.visible = True
                max_height = item.height

    def visible_count(self) -> int:
        count = 0
        for row in self._grid:
            count += sum([1 for tree in row if tree.visible])
        return count


if __name__ == "__main__":
    with open("../input.txt", "r") as infile:
        forest = infile.readlines()
    my_forest = Forest(len(forest), len(forest[0].strip()))
    my_forest.fill_forest(forest)
    my_forest.check_visibility()
    print(f"Visible Trees: {my_forest.visible_count()}")
