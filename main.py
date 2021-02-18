
def is_moved(piece_to_move, x, y, pieces):
    """
        Determine if a piece can be moved according to the
        type of piece, the board dimension and the other pieces
        positions.
    """
    x = translate_coordinates(x)    #Will be optimized with the others functions
    
    return (piece_to_move.mov(x, y) and
            board_limit(x, y) and
            someone_on_case(x, y, pieces["pawn"]))


def move_piece(piece_to_move, x, y, pieces):

    x = translate_coordinates(x)    #Will be optimized with the others functions

    new_pos = piece_to_move
    new_pos.x_pos = x
    new_pos.y_pos = y 

    pieces["pawn"][pieces["pawn"].index(piece_to_move)] = new_pos

    return pieces


def game_test():
    """
        Temporary "main" function to test the "is_moved" one.
    """
    pieces = {}
    #Will be with full pieces generation :
    pieces['pawn'] = test_generation_white_pawn()

    #Exemple :
    piece_to_move = find_piece_on_case("b", 2, pieces["pawn"])

    if is_moved(piece_to_move, "b", 3, pieces):
        pieces = move_piece(piece_to_move, "b", 3, pieces)


def find_piece_on_case(x, y, pieces):
    """
        Determine wich piece is on given coordinates
    """
    x = translate_coordinates(x)    #Will be optimized with the others functions

    for piece in pieces :
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
    translate_coordinates(x)    #Will be optimized with the others functions

    for piece in pieces :
        if piece.x_pos == x and piece.y_pos == y:
            return False

    return True


def translate_coordinates(x):
    """
        Translate chess x coordinate (str) to int.
    """
    try :
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


class Pawn:
    
    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to the
            pawn allowed moves.
        """
        return (x - self.x_pos == 0 and
                y - self.y_pos == 1)


class Bishop:
    
    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to the
            bishop allowed moves.
        """
        return (abs(x - self.x_pos) == abs(y - self.y_pos) and
                x - self.x_pos != 0)


class Knight:
    
    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            knight allowed moves.
        """
        return ((abs(x - self.x_pos) == 2 and
                abs(y - self.y_pos) == 1) or
                (abs(x - self.x_pos) == 1 and
                abs(y - self.y_pos) == 2))


class Rook:

    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            rook allowed moves.
        """
        return ((x - self.x_pos != 0 and
                y - self.y_pos == 0) or
                (x - self.x_pos == 0 and
                y - self.y_pos != 0)) 


class Queen:
    
    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident
        
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
                
                
class King:
    
    def __init__(self, x_pos, y_pos, ident):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            king allowed moves.
        """
        return (abs(x - self.x_pos) == 1 or
                abs(y - self.y_pos) == 1)


game_test()