import uuid
import random


class Minesweeper:
    """Instances of the Minesweeper class represent minesweeper game logic
    """    ''''''
    def __init__(self, mines: int, width: int, height: int, completed: bool = False,
                 open_field: list = None, field: list = None,
                 game_id: str = None, opend: int = 0) -> None:
        """Creates Minesweeper object

        Args:
            mines (int): quantity of mines
            width (int): width of game field
            height (int): height of game field
            completed (bool, optional): shows is game allready completed. Defaults to False.
            open_field (list, optional): game field, that is shown to a player. Defaults to None.
            field (list, optional): game field, that we store. Defaults to None.
            game_id (str, optional): id of this game. Defaults to None.
        """        ''''''
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
        self.opend = opend

    def set_bombs(self) -> None:
        """Set`s bombs on game field
        """        ''''''
        spot_numbers: list = [i for i in range(self.width * self.height)]
        random.shuffle(spot_numbers)
        bombs_spots: list = spot_numbers[:self.mines]
        count: int = 0
        for i in range(self.height):
            for j in range(self.width):
                if count in bombs_spots:
                    self.field[i][j] = 'M'
                    self.get_bombs_around(i, j)
                count += 1

    def get_bombs_around(self, i: int, j: int) -> None:
        """Show`s count of bombs in fields arond of given

        Args:
            i (int): row in wich given element is
            j (int): column in wich given element is
        """        ''''''
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (i + dy > -1 and i + dy < self.height
                    and j + dx > -1 and j + dx < self.width
                    and self.field[i + dy][j + dx] != 'M'):
                    self.field[i + dy][j + dx] += 1

    def start(self) -> None:
        self.set_bombs()

    def turn(self, row: int, col: int) -> None:
        """Open`s field by given coordinates

        Args:
            row (int): row in wich given element is
            col (int): column in wich given element is
        """        
        spot = self.field[row][col]
        if spot == 'M':
            self.loose()
        elif spot == 0:
            self.open_empty(row, col)
            self.is_won()
        elif spot in range(1, 8):
            self.open_field[row][col] = str(spot)
            self.opend += 1
            self.is_won()

    def open_empty(self, i: int, j: int) -> None:
        """Open`s elments around wihich there are no bombs

        Args:
            i (int): row in wich given element is
            j (int): column in wich given element is
        """        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (i + dy > -1 and i + dy < self.height
                    and j + dx > -1 and j + dx < self.width
                    and self.field[i + dy][j + dx] != 'M'
                    and self.open_field[i + dy][j + dx] == ' '):
                    spot = self.field[i + dy][j + dx]
                    self.open_field[i + dy][j + dx] = str(spot)
                    self.opend += 1
                    self.is_won()
                    if spot == 0:
                        self.open_empty(i + dy, j + dx)

    def is_won(self) -> None:
        if self.opend >= (self.width * self.height) - self.mines:
            self.win()

    def win(self) -> None:
        self.open_all(True)
        self.completed = True

    def loose(self) -> None:
        self.open_all(False)
        self.completed = True

    def open_all(self, is_won: bool) -> None:
        """Open`s all fields

        Args:
            is_won (bool): defines is player won 
        """        
        for i in range(self.height):
            for j in range(self.width):
                spot = self.field[i][j]
                if spot == 'M':
                    if is_won:
                        self.open_field[i][j] = 'M'
                    else:
                        self.open_field[i][j] = 'X' 
                else:
                    self.open_field[i][j] = str(self.field[i][j])


if __name__ == "__main__":
    game: Minesweeper  = Minesweeper(3, 5, 5)
    game.start()
    print(game.game_id)
    print(game.open_field)
    
    for i in game.field:
        for j in i:
            print(str(j), ' ', end='')
        print()
    while not game.completed:
        row = int(input())
        col = int(input())
        game.turn(row, col)
        for i in game.open_field:
            print(str(i))