from operator import mod
from unicodedata import name
import tools

def move_Peon(piece, f, c):
    tools.validate(piece.board, f,c)
    
    color = piece.color

    mov = []
    if color == "Negras":
        mov = [ [-1,0] , [-1,-1], [-1,1]]
    elif color == "Blancas":
        mov =  [[1,0] , [1,-1], [1,1]]

    if (piece.posf + mov[0][0], piece.posc + mov[0][1]) == (f,c):
        
        if piece.board[f,c] != None:
            raise Exception("Hay una pieza en la posición " + str((f,c)))
        
        else:
            piece.move_changepos(f,c)

        

    if (piece.posf + mov[1][0], piece.posc + mov[1][1]) == (f,c):
        
        if piece.board[f,c] == None:
            raise Exception("No hay ninnguna pieza para comer en la posición " + str((f,c)))

        else:
            piece.move_changepos(f,c)

    if (piece.posf + mov[2][0], piece.posc + mov[2][1]) == (f,c):
        
        if piece.board[f,c] == None:
            raise Exception("No hay ninnguna pieza para comer en la posición " + str((f,c)))

        else:
            piece.move_changepos(f,c)

def move_Rey(piece, f, c):
    tools.validate(piece.board, f,c)

    pos = [piece.posf, piece.posc]
    
    fdis = abs(f - pos[0])
    cdis = abs(c - pos[1])
    sum = fdis + cdis

    if sum != 0 and sum <= 2 and fdis != 2 and cdis != 2:
        return True
    else:
        raise Exception("Jugada Ilegal. La posición enviada no es un movimiento válido del " + piece.name)



def move_Alfil(piece, f, c):
    tools.validate(piece.board, f,c)

    pos = [piece.posf, piece.posc]
    dirf = (f - pos[0])
    
    if dirf < 0:
        dirf = -1
    elif dirf == 0:
        dirf = 0
    else:
        dirf = 1

    dirc = (c - pos[1])
    
    if dirc < 0:
        dirc = -1
    elif dirc == 0:
        dirc = 0
    else:
        dirc = 1
    

    if (dirf,dirc) == (0,0):
        raise Exception("No puede moverse a la misma posición el alfil")

    elif dirf == 0 or dirc == 0:
        raise Exception("El"+ name +"no se mueve por la columna")

    i = 1
    while i*dirf < piece.board.df and i*dirc < piece.board.dc:
        posnew = (i*dirf + pos[0], i*dirc + pos[1])

        if posnew == (f,c):
            return True

        elif piece.board.exist_piece(posnew[0],posnew[1]):
            raise Exception("Hay una pieza interceptando tu camino en la posición " + str((f,c)))
        i+=1
    
def move_Caballo(piece, f, c):
    tools.validate(piece.board, f,c)

    pos = [piece.posf, piece.posc]
    
    fdis = abs(f - pos[0])
    cdis = abs(c - pos[1])
    sum = fdis + cdis

    if sum == 3 and fdis != 3 and cdis != 3:
        return True
    else:
        raise Exception("Jugada Ilegal. La posición enviada no es un movimiento válido del " + piece.name)

def move_Torre(piece, f, c):
    tools.validate(piece.board, f,c)

    pos = [piece.posf, piece.posc]
    if f == pos[0]:
        dirc = (c - pos[1])
    
        if dirc < 0:
            dirc = -1
        elif dirc == 0:
            dirc = 0
        else:
            dirc = 1
    
        i = 1    
        while i*dirc < piece.board.df:
            posnew = (f,i*dirc + pos[0])

            if posnew == (f,c):
                return True

            elif piece.board.exist_piece(posnew[0],posnew[1]):
                raise Exception("Hay una pieza interceptando tu camino en la posición " + str((f,c)))
            i+=1
    

    elif c == pos[1]:
        dirf = (f - pos[0])
    
        if dirf < 0:
            dirf = -1
        elif dirf == 0:
            dirf = 0
        else:
            dirf = 1
        
        i = 1    
        while i*dirf < piece.board.df:
            posnew = (i*dirf + pos[0],c)

            if posnew == (f,c):
                return True

            elif piece.board.exist_piece(posnew[0],posnew[1]):
                raise Exception("Hay una pieza interceptando tu camino en la posición " + str((f,c)))
            i+=1
    

    else:
        raise Exception("Jugada Ilegal. La torre no se mueve en diagonal")

def move_Dama(piece, f, c):
    tools.validate(piece.board, f,c)

    pos = [piece.posf, piece.posc]
    if f == pos[0]:
        dirc = (c - pos[1])
    
        if dirc < 0:
            dirc = -1
        elif dirc == 0:
            dirc = 0
        else:
            dirc = 1
    
        i = 1    
        while i*dirc < piece.board.df:
            posnew = (f,i*dirc + pos[0])

            if posnew == (f,c):
                return True

            elif piece.board.exist_piece(posnew[0],posnew[1]):
                raise Exception("Hay una pieza interceptando tu camino en la posición " + str((f,c)))
            i+=1
    
    elif c == pos[1]:
        dirf = (f - pos[0])
    
        if dirf < 0:
            dirf = -1
        elif dirf == 0:
            dirf = 0
        else:
            dirf = 1
        
        i = 1    
        while i*dirf < piece.board.df:
            posnew = (i*dirf + pos[0],c)

            if posnew == (f,c):
                return True

            elif piece.board.exist_piece(posnew[0],posnew[1]):
                raise Exception("Hay una pieza interceptando tu camino en la posición " + str((f,c)))
            i+=1
    
    else:
        move_Alfil(piece, f, c)        

