import shared

class Solution:

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    def run(self):
        count = 0
        cals = 0
        elves = []

        calorieData = shared.fileToArray('day_1/'+self.inputFile)

        for x in calorieData:
            if (x == ''):
                print(f'{count}: {cals}')
                elves.append(cals)
                cals = 0
                count += 1
            else:
                cals += int(x)
                

        elves.sort(reverse=True)
    
        print(f'Total elves: {count}')    
        print(f'Highest calories: {elves[0]}')    