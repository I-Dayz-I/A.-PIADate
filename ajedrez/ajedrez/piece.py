from aifc import Error
from distutils.log import ERROR
from distutils.util import change_root
import tools

class Piece():
    def __init__(self,funMov, color, name_piece):
        self.fmov = funMov
        self.color = color
        self.type_piece = name_piece

    def insert(self, board, posf, posc):
        self.insert_board(board, posf, posc)

        board.insert_piece(self, posf, posc)

    def insert_board(self, board, posf, posc):
        tools.validate(board, posf,posc)
        self.board = board

        self.change_pos(posf, posc)


    def move(self, posf, posc):
        self.fmov(self,posf,posc)

    def change_pos(self, posf , posc):
        self.posf = posf
        self.posc = posc

    def move_changepos(self,f,c):
        self.board.changepos_piece(self,f,c)
        
    def name(self):
        return self.type_piece
        

        
    