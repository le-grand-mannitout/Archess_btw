
from piece import *

def is_moved(piece_to_move: Piece,
             x: int,
             y: int,
             pieces: dict) -> bool:
    """
        Determine if a piece can be moved according to the
        type of piece, the board dimension and the other pieces
        positions.
    """
    return (piece_to_move.mov(x, y) and
            board_limit(x, y) and
            someone_on_case(x, y, pieces["pawn"]))


def move_piece(piece_to_move: Piece,
               x: int,
               y: int,
               pieces: dict) -> dict:
    """
        Move a piece by changing piece coordinates on the pieces
        dictionnary.
    """
    new_pos = piece_to_move
    new_pos.x_pos = x
    new_pos.y_pos = y

    pieces["pawn"][pieces["pawn"].index(piece_to_move)] = new_pos

    return pieces


def get_user_input() -> list:
    """
        Get user play input, syntax must be: "pawntomove coordinates_to_go"
        ex: e2 e3.
    """
    play = input().split(" ")

    return play


def format_user_input(user_input: list) -> list:
    """
        Format user input to be interpretated by the chess program.
    """

    for coordinate in user_input:

        list_coordinate = list(coordinate)

        list_coordinate[0] = int(translate_coordinates(list_coordinate[0]))
        list_coordinate[1] = int(list_coordinate[1])

        user_input[user_input.index(coordinate)] = list_coordinate

    return user_input


def find_piece_on_case(x: int,
                       y: int,
                       pieces: dict) -> Piece:
    """
        Determine wich piece is on given coordinates.
    """
    for piece in pieces["pawn"]:
        if piece.x_pos == x and piece.y_pos == y:
            return piece


def test_generation_white_pawn() -> list:
    """
        Temporary pawn generation for testing the rules.
    """
    return [Pawn(piece_x + 1, 2, piece_x + 1) for piece_x in range(8)]


def someone_on_case(x: int,
                    y: int,
                    pieces: dict) -> bool:
    """
        Determine if a piece is on the same coordinates as
        the wanted one.
    """
    for piece in pieces:
        if piece.x_pos == x and piece.y_pos == y:
            return False

    return True


def translate_coordinates(x: str) -> int:
    """
        Translate chess x coordinate (str) to int.
    """
    try:
        LETTER_COORDINATES = ("abcdefgh")

        return LETTER_COORDINATES.index(x) + 1

    except TypeError:
        return x


def board_limit(x: int,
                y: int) -> bool:
    """
        Determine if move coordinates are included in the chess board.
    """
    return ((x > 0 and x <= 8) and
            (y > 0 and y <= 8))
