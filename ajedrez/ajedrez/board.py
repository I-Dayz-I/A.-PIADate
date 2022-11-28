import tools
from pickle import NONE


class Board():
    def __init__(self, df,dc):
        self.board = []
        for f in range(df):
            self.board.append([])
            for c in range(dc):
                self.board[f].append(None)
        self.df = df
        self.dc = dc

    def countF(self):
        return self.df

    def countC(self):
        return self.dc

    def insert(self,piece, posf, posc):
        self.insert_piece(piece, posf, posc)
        
        piece.insert_board(self, posf, posc)

    def insert_piece(self,piece, posf, posc):
        tools.validate(self, posf, posc)

        self.board[posf][posc] = piece

    def changepos_piece(self, piece, posf, posc):
        self.board[posf][posc] = piece
        self.board[piece.posf][piece.posc] = None

        piece.change_pos(posf, posc)

    def validate_piece(self, piece):
        if not piece.board == self:
            raise Exception("La pieza no se encuentra en este tablero")

    def move_pos(self, posif, posic, posf, posc):
        tools.validate(self, posif,posic)
        p = self.peek_piece(posif,posic)
        
        self.move_piece(self.peek_piece(posif,posic),posf, posc)

    def move_piece(self, piece, posf, posc):
        self.validate_piece(piece)
        
        piece.move(posf, posc)
        self.changepos_piece(piece, posf, posc)

    def exist_piece(self,f,c):
        if self.board[f][c] != None:
            return True
        return False

    def peek_piece(self,f,c):
        return self.board[f][c]
