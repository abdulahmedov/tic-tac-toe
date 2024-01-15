from board import Board
from players import Player, Rival, Turn

import random
import time


if __name__ == "__main__":
    board = Board()
    player = Player(board=board)
    rival = Rival(board=board)
    winner = None
    while not winner:
        user_turn = player.make_turn(board=board)
        board.process_turn(turn=user_turn)
        rival_turn = rival.make_turn(board=board)
        board.process_turn(turn=rival_turn)
        winner = board.check_winner()
    print(f'{winner} win !')
