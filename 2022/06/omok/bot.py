from typing import Sequence, Tuple
from .game import Game_no_str

# TODO Add docstrings


class Bot:
    def __init__(self, game=None) -> None:
        if isinstance(game, Game_no_str):
            self.game = game
        elif isinstance(game, int) and 0 < game:
            self.game = Game_no_str(game)
        else:
            self.game = Game_no_str()

    def import_board(self, board) -> bool:
        if not isinstance(board, Sequence):
            return False
        if not all(len(board) == len(col) for col in board):
            return False
        self.board = [list(col) for col in board]
        return True

    def eval(self):
        # TODO Evaluate current position
        pass

    def alpha_beta(self, depth, alpha, beta):
        # TODO Alpha beta pruning algorithm
        pass

    def best(self) -> Tuple(int, int):
        """
        Return the best move of current position.
        """
        # TODO Add best function
        pass

    def move(self, x, y):
        self.game.move(x, y)


if __name__ == '__main__':
    from .game import Game
    game = Game()
    bot = Bot()

    while True:
        print(game)
        while True:
            move = input("Move: ")
            if game.move(move):
                break
        if not game.playing:
            break
        bot.move(*game.move_to_tuple(move))

        move = bot.best()
        game.move_int(*move)
        if not game.playing:
            break
        bot.move(*move)

    print("Game Finished.")
