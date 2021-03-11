
def is_moved(piece_to_move, x, y, pieces):
    """
        Determine if a piece can be moved according to the
        type of piece, the board dimension and the other pieces
        positions.
    """
    return (piece_to_move.mov(x, y) and
            board_limit(x, y) and
            someone_on_case(x, y, pieces["pawn"]))


def move_piece(piece_to_move, x, y, pieces):
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


def format_user_input(user_input):
    """
        Format user input to be interpretated by the chess program.
    """

    for coordinate in user_input:

        list_coordinate = list(coordinate)

        list_coordinate[0] = int(translate_coordinates(list_coordinate[0]))
        list_coordinate[1] = int(list_coordinate[1])

        user_input[user_input.index(coordinate)] = list_coordinate

    return user_input


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


def find_piece_on_case(x, y, pieces):
    """
        Determine wich piece is on given coordinates.
    """
    for piece in pieces["pawn"]:
        if piece.x_pos == x and piece.y_pos == y:
            return piece

    return None


def test_generation_white_pawn():
    """
        Temporary pawn generation for testing the rules.
    """
    return [Pawn(piece_x + 1, 2, piece_x + 1) for piece_x in range(8)]


def someone_on_case(x, y, pieces):
    """
        Determine if a piece is on the same coordinates as
        the wanted one.
    """
    for piece in pieces:
        if piece.x_pos == x and piece.y_pos == y:
            return False

    return True


def translate_coordinates(x):
    """
        Translate chess x coordinate (str) to int.
    """
    try:
        LETTER_COORDINATES = ("abcdefgh")

        return LETTER_COORDINATES.index(x) + 1

    except TypeError:
        return x


def board_limit(x, y):
    """
        Determine if move coordinates are included in the chess board.
    """
    return ((x > 0 and x <= 8) and
            (y > 0 and y <= 8))


class Piece:

    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident


class Pawn(Piece):

    def mov(self, x, y):
        """
            Determine if movement is correct according to the
            pawn allowed moves.
        """
        return (x - self.x_pos == 0 and
                y - self.y_pos == 1)


class Bishop(Piece):

    def mov(self, x, y):
        """
            Determine if movement is correct according to the
            bishop allowed moves.
        """
        return (abs(x - self.x_pos) == abs(y - self.y_pos) and
                x - self.x_pos != 0)


class Knight(Piece):

    def mov(self, x, y):
        """
            Determine if movement is correct according to
            knight allowed moves.
        """
        return ((abs(x - self.x_pos) == 2 and
                abs(y - self.y_pos) == 1) or
                (abs(x - self.x_pos) == 1 and
                abs(y - self.y_pos) == 2))


class Rook(Piece):

    def mov(self, x, y):
        """
            Determine if movement is correct according to
            rook allowed moves.
        """
        return ((x - self.x_pos != 0 and
                y - self.y_pos == 0) or
                (x - self.x_pos == 0 and
                y - self.y_pos != 0))


class Queen(Piece):

    def mov(self, x, y):
        """
            Determine if movement is correct according to
            queen allowed moves.
        """
        return ((abs(x - self.x_pos) == abs(y - self.y_pos) and
                x - self.x_pos != 0) or
                ((x - self.x_pos != 0 and
                 y - self.y_pos == 0) or
                (x - self.x_pos == 0 and
                 y - self.y_pos != 0)))


class King(Piece):

    def mov(self, x, y):
        """
            Determine if movement is correct according to
            king allowed moves.
        """
        return (abs(x - self.x_pos) == 1 or
                abs(y - self.y_pos) == 1)


game_test()
