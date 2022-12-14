import shared
from shared import bcolours

class Solution:
    RED_SQUARE = '🟥'
    GREEN_SQUARE = '🟩'

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    def is_overlap(self, range_1, range_2):
        r_1 = []
        r_2 = []

        for x in range(int(range_1[0]), (int(range_1[1]))+1):
            r_1.append(x)

        for x in range(int(range_2[0]), (int(range_2[1]))+1):
            r_2.append(x)

        overlap = set(r_1).intersection(r_2)            

        if overlap:
            return True
        return False


    def get_range(self, pair):
        range_1 = pair[0].split('-')
        range_2 = pair[1].split('-')

        return range_1, range_2

    def visualiseRange(self, range):
        i = 1
        while i <= 100:
            if i < int(range[0]) or i > int(range[1]):
                print(self.RED_SQUARE, end='')
            else:
                print(self.GREEN_SQUARE, end='')
            i += 1
        print('')

    def run(self):
        """all the elven magic happens here
        """
        pairs = 0
        overlapped = 0

        pair_data = shared.fileToArray('day_4/'+self.inputFile)

        for pair in pair_data:
            pairs += 1
            pair = pair.split(',')
            
            if self.debug:
                print(f'pair {pairs}: {pair}')

            range_1, range_2 = self.get_range(pair)      

            print(f'{range_1} - {range_2}')
            self.visualiseRange(range_1)         
            self.visualiseRange(range_2)     

            if self.is_overlap(range_1, range_2) :
                overlapped += 1
                if self.debug:
                    print(f'{bcolours.OKBLUE} {pairs} {bcolours.ENDC}')

            if self.debug:
                print(f'-------')                


        print(f'Total pairs: {pairs}')
        print(f'Total overlapped: {overlapped}')
