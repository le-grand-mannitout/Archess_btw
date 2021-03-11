
import sys
sys.path.insert(0, '..')

from main import *

def game_test():
    """
        Temporary function to test the implemented basic games mechanics.
    """
    pieces = {}
    # Will be with full pieces generation :
    pieces['pawn'] = test_generation_white_pawn()

    while 1:
        user_input = format_user_input(get_user_input())

        co_to_move = user_input[0]
        x, y = user_input[1][0], user_input[1][1]

        piece_to_move = find_piece_on_case(co_to_move[0],
                                           co_to_move[1],
                                           pieces)

        if is_moved(piece_to_move, x, y, pieces):
            pieces = move_piece(piece_to_move, x, y, pieces)

game_test()
