import sys

class CheckerBoard:
    def __init__(self):
        self.board = [['_'] * 8 for _ in range(8)]
        self.board[0][1::2] = ['W'] * 4
        self.board[1][::2] = ['W'] * 4
        self.board[2][::2] = ['W'] * 4
        self.board[5][1::2] = ['B'] * 4
        self.board[6][::2] = ['B'] * 4
        self.board[7][1::2] = ['B'] * 4

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.board)


board = CheckerBoard()
print(board)