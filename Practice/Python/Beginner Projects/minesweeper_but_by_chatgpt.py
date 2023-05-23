# MINESWEEPER game by chatgpt because I'm lazy, with a few changes to make it better.

import random

class Minesweeper:
    def __init__(self, size=8, mines=10):
        self.size = size
        self.mines = mines
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.visible_board = [['-' for _ in range(size)] for _ in range(size)]
        self.game_over = False

        # Set up the mines randomly
        for i in range(mines):
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            while self.board[row][col] == 'X':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - 1)
            self.board[row][col] = 'X'

        # Fill in the rest of the board with numbers indicating the number of adjacent mines
        for row in range(size):
            for col in range(size):
                if self.board[row][col] == 'X':
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        r = row + i
                        c = col + j
                        if r < 0 or r >= size or c < 0 or c >= size:
                            continue
                        if self.board[r][c] == 'X':
                            self.board[row][col] += 1

    def show_board(self):
        print('   ', end='')
        for col in range(self.size):
            print(f'  {chr(ord("A") + col)} ', end='')
        print()
        print('    ' + '----' * self.size)
        for row in range(self.size):
            print(f'{self.size - row:>2} |', end='')
            for col in range(self.size):
                print(f' {self.visible_board[row][col]} |', end='')
            print('')
        print('   ', end='')
        for col in range(self.size):
            print(f'  {chr(ord("A") + col)} ', end='')
        print()

    def reveal(self, row, col):
        if self.board[row][col] == 'X':
            self.visible_board[row][col] = 'X'
            self.game_over = True
            print('Game over!')
        elif self.board[row][col] > 0:
            self.visible_board[row][col] = str(self.board[row][col])
        else:
            self.visible_board[row][col] = ' '
            for i in range(-1, 2):
                for j in range(-1, 2):
                    r = row + i
                    c = col + j
                    if r < 0 or r >= self.size or c < 0 or c >= self.size:
                        continue
                    if self.visible_board[r][c] == '-':
                        self.reveal(r, c)

    def play(self):
        while not self.game_over:
            self.show_board()
            move = input('Enter row and column to reveal (e.g. A3): ')
            col = ord(move[0].upper()) - ord('A')
            row = self.size - int(move[1:])
            self.reveal(row, col)
        self.show_board()

game = Minesweeper()
game.play()
