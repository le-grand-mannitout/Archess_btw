
class Piece:

    def __init__(self, x_pos: int,
                 y_pos: int,
                 ident: int):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ident = ident


class Pawn(Piece):

    def mov(self, x: int, y: int) -> bool:
        """
            Determine if movement is correct according to the
            pawn allowed moves.
        """
        return (x - self.x_pos == 0 and
                y - self.y_pos == 1)


class Bishop(Piece):

    def mov(self, x: int, y: int) -> bool:
        """
            Determine if movement is correct according to the
            bishop allowed moves.
        """
        return (abs(x - self.x_pos) == abs(y - self.y_pos) and
                x - self.x_pos != 0)


class Knight(Piece):

    def mov(self, x: int, y: int) -> bool:
        """
            Determine if movement is correct according to
            knight allowed moves.
        """
        return ((abs(x - self.x_pos) == 2 and
                abs(y - self.y_pos) == 1) or
                (abs(x - self.x_pos) == 1 and
                abs(y - self.y_pos) == 2))


class Rook(Piece):

    def mov(self, x: int, y: int) -> bool:
        """
            Determine if movement is correct according to
            rook allowed moves.
        """
        return ((x - self.x_pos != 0 and
                y - self.y_pos == 0) or
                (x - self.x_pos == 0 and
                y - self.y_pos != 0))


class Queen(Piece):

    def mov(self, x: int, y: int) -> bool:
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

    def mov(self, x: int, y: int) -> bool:
        """
            Determine if movement is correct according to
            king allowed moves.
        """
        return (abs(x - self.x_pos) == 1 or
                abs(y - self.y_pos) == 1)

