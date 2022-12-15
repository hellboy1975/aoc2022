import shared
from shared import baseSolution

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

class Solution(baseSolution):

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

        if (cls.debug):
            print(f'  outcome: {outcome} value: {value}')

        
        if (play == ROCK):
            score = ROCK_SCORE
            if (outcome == TO_LOSE):
                score = SCISSOR_SCORE
            elif (outcome == TO_WIN):
                score = PAPER_SCORE

        elif (play == PAPER):
            score = PAPER_SCORE
            if (outcome == TO_LOSE):
                score = ROCK_SCORE
            elif (outcome == TO_WIN):
                score = SCISSOR_SCORE

        elif (play == SCISSORS):
            score = SCISSOR_SCORE
            if (outcome == TO_LOSE):
                score = PAPER_SCORE
            elif (outcome == TO_WIN):
                score = ROCK_SCORE

        if (cls.debug):
            print(f'  play: {play} score: {score}')
        return score, value
            




    def run(self):
        roundTotal = rounds = total = 0

        gameData = shared.fileToArray('day_2/'+self.inputFile)

        for x in gameData:
            x = x.split(' ')
            if (self.debug):
                print(x)

            score, value = self.processRound(play = x[0], outcome = x[1])

            # TODO: 
            roundTotal = score + value
            if (self.debug):
                print(f'score: {score} value: {value} total: {roundTotal}')

            total += roundTotal
            rounds += 1
                
        print(f'Total rounds: {rounds}')     
        print(f'Total score: {total}') 