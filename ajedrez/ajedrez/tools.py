from board import *
from piece import *
import movement
import glob
from operator import truediv

def validate(board, f,c):
    if not (0 < f+1 and f < board.df and 0 < c+1 and c <  board.dc):
        raise Exception("Las posiciones " + str((f,c)) + " no son válidas")

def create_board():
    glob.board = Board(8,8)

def print_board():
    for f in range(1,glob.board.countF()+1):
        print("| ", end="")
        for c in range(0,glob.board.countC()):
            if glob.board.peek_piece(glob.board.countF()-f,c) == None:
                print("*", end="")
            else:
                print(glob.board.peek_piece(glob.board.countF()-f,c).name()[0],end="")
            print(" | ", end="")
        print()

def insert_initial_piece():
    # Blancas
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,0)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,1)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,2)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,3)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,4)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,5)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,6)
    glob.board.insert(Piece(movement.move_Peon, "Blancas", "Peon"),1,7)

    glob.board.insert(Piece(movement.move_Torre   ,"Blancas", "Torre"),0,0)
    glob.board.insert(Piece(movement.move_Caballo ,"Blancas", "Caballo"),0,1)
    glob.board.insert(Piece(movement.move_Alfil   ,"Blancas", "Alfil"),0,2)
    glob.board.insert(Piece(movement.move_Dama    ,"Blancas", "Dama"),0,3)
    glob.board.insert(Piece(movement.move_Rey     ,"Blancas", "Rey"),0,4)
    glob.board.insert(Piece(movement.move_Alfil   ,"Blancas", "Alfil"),0,5)
    glob.board.insert(Piece(movement.move_Caballo ,"Blancas", "Caballo"),0,6)
    glob.board.insert(Piece(movement.move_Torre   ,"Blancas", "Torre"),0,7)

    # Negras
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,0)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,1)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,2)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,3)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,4)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,5)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,6)
    glob.board.insert(Piece(movement.move_Peon, "Negras", "Peon"),6,7)

    glob.board.insert(Piece(movement.move_Torre   , "Negras", "Torre"),7,0)
    glob.board.insert(Piece(movement.move_Caballo , "Negras", "Caballo"),7,1)
    glob.board.insert(Piece(movement.move_Alfil   , "Negras", "Alfil"),7,2)
    glob.board.insert(Piece(movement.move_Dama    , "Negras", "Dama"),7,3)
    glob.board.insert(Piece(movement.move_Rey     , "Negras", "Rey"),7,4)
    glob.board.insert(Piece(movement.move_Alfil   , "Negras", "Alfil"),7,5)
    glob.board.insert(Piece(movement.move_Caballo , "Negras", "Caballo"),7,6)
    glob.board.insert(Piece(movement.move_Torre   ,"Negras", "Torre"),7,7)