from tools import *
import glob

def main():
    create_board()
    insert_initial_piece()

    print_board()

    glob.board.move_pos(1,4, 3,4)
    print("")
    print_board()

    glob.board.move_pos(0,3, 2,5)
    print("")
    print_board()
    
    glob.board.move_pos(0,5, 3,2)
    print("")
    print_board()
    
    glob.board.move_pos(1,0, 3,0)
    print("")
    print_board()
    
    glob.board.move_pos(0,0, 2,0)
    print("")
    print_board()

    glob.board.move_pos(0,1, 2,2)
    print("")
    print_board()
    
    glob.board.move_pos(0,4, 0,5)
    print("")
    print_board()
    

main()