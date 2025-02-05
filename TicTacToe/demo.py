from game import Game
from player import Player

class TicTacToe:
    @staticmethod
    def run():
        player1 = Player("John","X")
        player2 = Player("Doe","O")
        game = Game(player1,player2)
        game.play()

if __name__ == "__main__":
    TicTacToe.run()