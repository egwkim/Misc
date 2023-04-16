class ConnectFourBoard:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.turn = 1
        self.ply = 0
        self.finished = False
        self.winner = 0
        self.symbols = [' ', 'O', 'X']

    def move(self, column):
        if self.finished:
            return False
        if column < 0 or column >= self.width:
            return False
        if self.board[0][column] != 0:
            return False

        for row in range(self.height - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.turn
                break
        self.ply += 1
        self.turn = 3 - self.turn

        self.finished = self.ply >= self.width * self.height or self.check_win()
        return True

    def check_win(self):
        for row in range(self.height):
            for column in range(self.width):
                if self.board[row][column] != 0:
                    if self.check_horizontal(row, column) or self.check_vertical(row, column) or self.check_diagonal(row, column):
                        self.winner = self.board[row][column]
                        return True
        return False

    def check_horizontal(self, row, column):
        for i in range(4):
            if column + i >= self.width or self.board[row][column + i] != self.board[row][column]:
                return False
        return True

    def check_vertical(self, row, column):
        for i in range(4):
            if row + i >= self.height or self.board[row + i][column] != self.board[row][column]:
                return False
        return True

    def check_diagonal(self, row, column):
        for i in range(4):
            if row + i >= self.height or column + i >= self.width or self.board[row + i][column + i] != self.board[row][column]:
                return False
        return True

    def __str__(self):
        s = ""
        for row in self.board:
            for cell in row:
                s += self.symbols[cell]
            s += "\n"
        return s


def main():
    while 1:
        mode = input('Number of players (1 or 2): ')
        if mode == '1' or mode == '2':
            break


if __name__ == '__main__':
    main()
