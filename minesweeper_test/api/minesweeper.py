import uuid
import random


class Minesweeper:

    def __init__(self, mines: int, width: int, height: int, completed: bool = False,
                 open_field: list = None, field: list = None,
                 game_id: str = None,) -> None:
        self.mines = mines
        self.width = width
        self.height = height
        if open_field is None:
            self.open_field = [[' ' for j in range(self.width)] for i in range(self.height)]
        else:
            self.open_field = open_field
        if field is None:
            self.field = [[0 for j in range(self.width)] for i in range(self.height)]
        else:
            self.field = field
        if game_id is None:
            self.game_id = str(uuid.uuid1())
        else:
            self.game_id = game_id
        self.completed = completed

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
    
    def start(self) -> None:
        self.set_bombs()

    def turn(self, row: int, col: int) -> None:
        spot = self.field[row][col]
        if spot == 'M':
            self.lose()
        elif spot == 0:
            self.open_empty(row, col)
        elif spot in range(1, 8):
            self.open_field[row][col] = str(spot)
    
    def open_empty(self, i: int, j: int) -> None:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (i + dy > -1 and i + dy < self.height
                    and j + dx > -1 and j + dx < self.width
                    and self.field[i + dy][j + dx] != 'M'
                    and self.open_field[i + dy][j + dx] == ' '):
                    spot = self.field[i + dy][j + dx]
                    self.open_field[i + dy][j + dx] = str(spot)
                    if spot == 0:
                        self.open_empty(i + dy, j + dx)
    
    def win(self) -> None:
        pass
    
    def lose(self) -> None:
        pass
        

if __name__ == "__main__":
    game: Minesweeper  = Minesweeper(3, 5, 5)
    game.start()
    print(game.game_id)
    print(game.open_field)
    
    for i in game.field:
        for j in i:
            print(str(j), ' ', end='')
        print()
    row = int(input())
    col = int(input())
    game.turn(row, col)
    for i in game.open_field:
        print(str(i))