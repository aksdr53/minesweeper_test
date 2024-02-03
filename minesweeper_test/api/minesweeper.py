import uuid
import random


class Minesweeper:

    def __init__(self, mines: int, width: int, height: int) -> None:
        self.mines = mines
        self.width = width
        self.height = height
        self.open_field: list = [[' ' for j in range(width)] for i in range(height)]
        self.field: list = [[0 for j in range(width)] for i in range(height)]
        self.id: str = str(uuid.uuid1())

    def set_bombs(self) -> None:
        spot_numbers: list = [i for i in range(self.width * self.height)]
        random.shuffle(spot_numbers)
        bombs_spots: list = spot_numbers[:self.mines]
        print(bombs_spots)
        count: int = 0
        for i in range(self.height):
            for j in range(self.width):
                if count in bombs_spots:
                    self.field[i][j] = 'M'
                    self.get_bombs_around(i, j)
                count += 1

    
    def get_bombs_around(self, i: int, j: int) -> None:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (i + dy > -1 and i + dy < self.height
                    and j + dx > -1 and j + dx < self.width
                    and self.field[i + dy][j + dx] != 'M'):
                    self.field[i + dy][j + dx] += 1


if __name__ == "__main__":
    game: Minesweeper  = Minesweeper(10, 5, 5)
    print(game.id)
    print(game.open_field)
    game.set_bombs()
    for i in game.field:
        print(str(i))