from board import Board, Turn

from typing import Protocol
import random
import time


class Player(Protocol):
    def make_turn(self) -> Turn:
        """dfvnlfksjnvlfksd"""
    
    def think() -> None:
        time.sleep(random.randint(1, 5))


class User(Player):
    def __init__(self, board: Board) -> None:
        self.weapon = board.user_weapon
    
    def make_turn(self, board: Board) -> Turn:
        correct_row = False
        while not correct_row:
            row = input('Type row: ')
            if row.isdigit():
                row = int(row)
                row -= 1
                if row >= 0 and row < len(board.grid):
                    if None in board.grid[row]:
                        correct_row = True
                    else:
                        print('There is no free space in this row. Choose another row.')
                else:
                    print('Your row out of bounds. Try again.')
            else:
                print("It's not digit. Try again.")

        correct_col = False
        while not correct_col:
            col = input('Type col: ')
            if col.isdigit():
                col = int(col)
                col -= 1
                if col >= 0 and col < len(board.grid):
                    if board.grid[row][col] is None:
                        correct_col = True
                    else:
                        print('There is no free space. Choose another col.')
                else:
                    print('Your col out of bounds. Try again.')
            else:
                print("It's not digit. Try again.")
        turn = Turn(row=row, col=col, weapon=self.weapon)
        return turn


class Rival(Player):
    def __init__(self, board: Board) -> None:
        self.weapon = board.rival_weapon
    
    def make_turn(self, board: Board) -> Turn:
        turn = Turn(row=None, col=None, weapon=self.weapon)
        while turn.row is None:
            row = random.choice(range(len(board.grid)))
            if None in board.grid[row]:
                turn.row = row
        while turn.col is None:
            col = random.choice(range(len(board.grid[row])))
            if board.grid[row][col] is None:
                turn.col = col
        self.think()
        print('Rivals turn...')
        self.think()
        return turn
