import shared

#scores
ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSOR_SCORE = 3

#values
WIN = 6
DRAW = 3
LOSE = 0

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

TO_LOSE = 'X'
TO_DRAW = 'Y'
TO_WIN = 'Z'

class Solution:

    

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    

    def playValue(cls, play):
        # this function will determine the score the player gets based on their selection
        if (play == ROCK):
            return ROCK_SCORE
        elif (play == PAPER):
            return PAPER_SCORE

        return SCISSOR_SCORE

    def processRound(cls, play, outcome):
        
        value = DRAW
        if (outcome == TO_WIN):
            value = WIN
        elif (outcome == TO_LOSE):
            value = LOSE

        print(f'  {value} value: {value}')

        score = 0
        if (play == ROCK):
            if (outcome == TO_LOSE):
                score = SCISSOR_SCORE
            elif (outcome == TO_WIN):
                score = PAPER_SCORE

        elif (play == PAPER):
            if (outcome == TO_LOSE):
                score = ROCK_SCORE
            elif (outcome == TO_WIN):
                score = SCISSOR_SCORE

        elif (play == SCISSORS):
            if (outcome == TO_LOSE):
                score = PAPER_SCORE
            elif (outcome == TO_WIN):
                score = ROCK_SCORE

        print(f'  {play} play: {play}')
        return score, value
            




    def run(self):
        roundTotal = rounds = total = 0

        gameData = shared.fileToArray('day_2/'+self.inputFile)

        for x in gameData:
            x = x.split(' ')
            if (self.debug):
                print(x)

            score, value = self.processRound(x[1], x[0])

            # TODO: 
            roundTotal = score + value
            if (self.debug):
                print(f'score: {score} value: {value} total: {roundTotal}')

            total += roundTotal
            rounds += 1
                
        print(f'Total rounds: {rounds}')     
        print(f'Total score: {total}') 