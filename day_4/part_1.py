import shared
from shared import bcolours
from shared import baseSolution

class Solution(baseSolution):
    RED_SQUARE = '🟥'
    GREEN_SQUARE = '🟩'

    def is_within_range(self, subject, range):
        """determines if a range (subject) is within another range

        Args:
            subject (array): an array to be compared to the range
            range (array): an array used for the comparison

        Returns:
            boolean: whether or not the subject is completely within the range
        """

        if self.debug:
            print(f'subject {subject[0]} <= {range[0]}')
            print(f'subject {subject[1]} >= {range[1]}')

        if int(subject[0]) <= int(range[0]) and int(subject[1]) >= int(range[1]):
            return True

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
        in_range = 0

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

            # if self.debug:
                # print(f'range 1: {range_1}')
                # print(f'range 2: {range_2}')

            if self.is_within_range(range_1, range_2) or self.is_within_range(range_2, range_1):
                in_range += 1
                if self.debug:
                    print(f'{bcolours.OKBLUE} {pairs} {bcolours.ENDC}')

            if self.debug:
                print(f'-------')                


        print(f'Total pairs: {pairs}')
        print(f'Total in range: {in_range}')
