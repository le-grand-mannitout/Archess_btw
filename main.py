
def is_moved(piece, x, y):
    """
        Determine if a piece can be move according to the
        type of piece and the board dimension
    """
    x = translate_coordinates(x)
    
    return (piece.mov(x, y) and
            board_limit(x, y))


def translate_coordinates(x):
    """
        Translate chess x coordinate (str) to int 
    """
    try :
        LETTER_COORDINATES = ("abcdefgh")
        
        return LETTER_COORDINATES.index(x) + 1    
 
    except TypeError:
        return x


def board_limit(x, y):
    """
        Determine if move coordinates are included in the chess board
    """
    return ((x > 0 and x <= 8) and
            (y > 0 and y <= 8))


class Pawn:
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to the
            pawn allowed moves
        """
        return (x - self.x_pos == 0 and
                y - self.y_pos == 1)


class Bishop:
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to the
            bishop allowed moves
        """
        return (abs(x - self.x_pos) == abs(y - self.y_pos) and
                x - self.x_pos != 0)


class Knight:
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            knight allowed moves
        """
        return ((abs(x - self.x_pos) == 2 and
                abs(y - self.y_pos) == 1) or
                (abs(x - self.x_pos) == 1 and
                abs(y - self.y_pos) == 2))


class Rook:

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            rook allowed moves
        """
        return ((x - self.x_pos != 0 and
                y - self.y_pos == 0) or
                (x - self.x_pos == 0 and
                y - self.y_pos != 0)) 
                
                
class Queen:
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            queen allowed moves
        """
        return ((abs(x - self.x_pos) == abs(y - self.y_pos) and
                x - self.x_pos != 0) or
                ((x - self.x_pos != 0 and
                y - self.y_pos == 0) or
                (x - self.x_pos == 0 and
                y - self.y_pos != 0)))
                
                
class King:
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def mov(self, x, y):
        """
            Determine if movement is correct according to
            king allowed moves
        """
        return (abs(x - self.x_pos) == 1 or
                abs(y - self.y_pos) == 1)
