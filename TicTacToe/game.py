from board import Board
from player import Player

class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1
    
    def play(self):
        self.board.print_board()
        while not self.board.is_full() and not self.board.is_winner():
            rows = int(input("Enter row: "))
            cols = int(input("Enter col: "))
            try:
                self.board.make_move(rows,cols,self.current_player.get_symbol())
                self.board.print_board()
                self.switchPlayer()
            except:
                print("Invalid move")
        if self.board.is_winner():
            print("ddsdsds")
            self.switchPlayer()
            print(f"{self.current_player.get_name()} wins")
        else:
            print("Draw")
    
    def switchPlayer(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    
    