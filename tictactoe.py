
# coding: utf-8

# In[10]:


from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player
#Inherit the class from the TwoPlayerGame class to handle all operations of the game
#define the players and the player who is going to start the game
class TicTacToe_game(TwoPlayersGame):
    def __init__(self, players):
        self.players = players
        self.nplayer = 1

        #Define the type of board
        self.board = [0] * 9

        #Define possible moves:
    def possible_moves(self):
        return [x+1 for x, y in enumerate(self.board) if y == 0]

        #Define the move of a player
    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

        #define when a player makes a move
    def umake_move(self, move):
        self.board[int(move) - 1] = 0

         #Define the lose condition that an opponent have three in a line
    def condition_for_lose(self):
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        return any([all([(self.board[z-1] == self.nopponent)
                for z in combination]) for combination in possible_combinations])

        #Define a check for the finish of game
    def is_over(self):
        return (self.possible_moves() == []) or self.condition_for_lose()

    #Show the current position of the players in the game
    def show(self):
        print('\n'+'\n'.join([' '.join([['.', 'O', 'X'][self.board[3*j + i]]
                for i in range(3)]) for j in range(3)]))

     #Compute the scores.
    def scoring(self):
        return -100 if self.condition_for_lose() else 0

    #Define the main method to define the algorithm and start the game:
if __name__ == "__main__":
    algo = Negamax(7)

    game = TicTacToe_game([Human_Player(), AI_Player(algo)])
    game.play()

# print the result
    if game.condition_for_lose():
        print ('\nPlayer', game.nopponent, 'wins.')
    else:
        print("\n It's a draw.")
