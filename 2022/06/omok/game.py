import string
from typing import Tuple

# TODO Handle possible errors
# TODO Add docstrings


class Game_no_str:
    def __init__(self, size=15) -> None:
        self.size = size
        self.board = [[0]*size for i in range(size)]
        self.playing = True
        self.player = 1
        self.ply = 0
        self.moves = []

    def switch(self) -> None:
        self.player = 3 - self.player

    def undo(self) -> bool:
        if len(self.moves) == 0:
            return False
        x, y = self.moves.pop()
        self.board[x][y] = 0
        self.playing = True
        self.switch()
        return True

    def move(self, x: int, y: int) -> bool:
        # TODO Check after each move
        if self.board[x][y] != 0:
            return False
        self.board[x][y] = self.player
        self.switch()
        self.ply += 1
        self.moves.append((x, y))
        return True

    def check_move(self, x: int, y: int):
        """
        Check if the specific move ends the game.
        """
        if self.board[x][y] == 0:
            self.move_int(x, y)
            result = self.check_move(x, y)
            self.undo()
            return result
        # TODO Check move

        # Draw
        if self._check_draw():
            self.playing = False
            return 3

    def check(self) -> int:
        # TODO Check win

        # Draw
        if self._check_draw():
            self.playing = False
            return 3

        # Still playing
        return 0

    def _check_draw(self):
        return self.ply == self.size**2


class Game(Game_no_str):
    def __init__(self, size=15) -> None:
        super().__init__(size)
        self.moves_str = []

    def __str__(self) -> str:
        # TODO Add __str__ function
        string = ""
        for col in self.board:
            for i in col:
                string += str(i)
            string += "\n"
        return string

    def undo(self) -> bool:
        result = super().undo()
        if result:
            self.moves_str.pop()
        return result

    def move_to_tuple(self, move: str) -> Tuple[int, int]:
        x = ord(move[0].upper()) - 65
        y = int(move[1:]) - 1
        return (x, y)

    def move_to_str(self, x: int, y: int) -> str:
        return string.ascii_uppercase[x] + str(y+1)

    def move(self, move: str) -> bool:
        try:
            if not move[0].isalpha:
                raise ValueError
            if not move[1:].isdigit():
                raise ValueError
            x, y = self.move_to_tuple(move)
            result = super().move(x, y)
            if result:
                self.moves_str.append(move)
            return result
        except ValueError:
            print("Invalid move.\n")
        except IndexError:
            print("Invalid move.\n")
        return False

    def move_int(self, x: int, y: int) -> bool:
        result = super().move(x, y)
        if result:
            self.moves_str.append(self.move_to_str(x, y))
        return result


if __name__ == '__main__':
    game = Game()
    while(game.playing):
        print(game)
        move = input("Move: ")
        game.move(move)
    print("Game Finished.")
