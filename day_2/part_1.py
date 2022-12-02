import shared

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSOR_SCORE = 3

WIN = 6
DRAW = 3
LOSE = 0

PLAYER_ROCK = 'A'
PLAYER_PAPER = 'B'
PLAYER_SCISSORS = 'C'

OPPONENT_ROCK = 'X'
OPPONENT_PAPER = 'Y'
OPPONENT_SCISSORS = 'Z'

class Solution:

    

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    

    def playValue(cls, play):
        # this function will determine the score the player gets based on their selection
        if (play == OPPONENT_ROCK):
            return ROCK_SCORE
        elif (play == OPPONENT_PAPER):
            return PAPER_SCORE

        return SCISSOR_SCORE

    def roundScore(cls, player, opponent):
        print(f'player: {player} opponent: {opponent}')

        # will return the score this round based on the win/loss/draw condition
        if (player == PLAYER_ROCK):
            if (opponent == OPPONENT_PAPER):
                return WIN
            elif (opponent == OPPONENT_SCISSORS):
                return LOSE

        if (player == PLAYER_PAPER):
            if (opponent == OPPONENT_SCISSORS):
                return WIN
            elif (opponent == OPPONENT_ROCK):
                return LOSE

        if (player == PLAYER_SCISSORS):
            if (opponent == OPPONENT_ROCK):
                return WIN
            elif (opponent == OPPONENT_PAPER):
                return LOSE

        return DRAW



    def run(self):
        roundTotal = rounds = total = 0

        gameData = shared.fileToArray('day_2/'+self.inputFile)

        for x in gameData:
            x = x.split(' ')
            if (self.debug):
                print(x)

            score = self.roundScore(x[0], x[1])
            value = self.playValue(x[1])
            roundTotal = score + value
            if (self.debug):
                print(f'score: {score} value: {value} total: {roundTotal}')

            total += roundTotal
            rounds += 1
                
        print(f'Total rounds: {rounds}')     
        print(f'Total score: {total}') 