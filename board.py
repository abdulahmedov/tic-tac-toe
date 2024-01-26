from dataclasses import dataclass
import random


def create_empty_grid():
    pass


@dataclass
class Turn:
    row: int
    col: int
    weapon: str


class Board:
    nought = 'O'
    cross = 'X'

    def __init__(self) -> None:
        print('Welcome!')
        self.user_weapon = random.choice([self.cross, self.nought])
        self.rival_weapon = self.cross if self.user_weapon == self.nought else self.nought

        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def show_grid(self) -> None:
        for i, row in enumerate(self.grid):
            row = list(map(lambda x: ' ' if x is None else x, row))
            row = ' | '.join(row)
            print(row)
            if i < len(self.grid) - 1:
                print('_' * len(row))

    def process_turn(self, turn: Turn) -> None:
        turn_processed = False
        while not turn_processed:
            if self.grid[turn.row][turn.col] is None:
                self.grid[turn.row][turn.col] = turn.weapon
                turn_processed = True
            else:
                print('This space already filled')
        self.show_grid()
    
    def check_winner(self):
        weapon_of_victory = None
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            weapon_of_victory = self.grid[0][0]
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            weapon_of_victory = self.grid[1][1]
        elif self.grid[0][0] == self.grid[1][0] == self.grid[2][0]:
            weapon_of_victory = self.grid[0][0]
        elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1]:
            weapon_of_victory = self.grid[0][1]
        elif self.grid[0][2] == self.grid[1][2] == self.grid[2][2]:
            weapon_of_victory = self.grid[0][2]
        elif self.grid[0][0] == self.grid[0][1] == self.grid[0][2]:
            weapon_of_victory = self.grid[0][0]
        elif self.grid[1][0] == self.grid[1][1] == self.grid[1][2]:
            weapon_of_victory = self.grid[1][0]
        elif self.grid[2][0] == self.grid[2][1] == self.grid[2][2]:
            weapon_of_victory = self.grid[2][0]
        if weapon_of_victory:
            winner = 'User' if weapon_of_victory == self.user_weapon else 'AI'
            return winner
