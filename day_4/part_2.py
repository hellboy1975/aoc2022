import string
import shared

class Solution:
    """ Solution for Day 3 Part 2
    """

    def __init__(self, debug):
        self.debug = debug

        self.input_file = 'data.txt'
        if debug:
            self.input_file = 'debug_data.txt'

    def run(self):
        """all the elven magic happens here
        """
        pairs = 0

        pair_data = shared.fileToArray('day_4/'+self.inputFile)

        for pair in pair_data:
            pairs += 1
            pair = pair.split(',')
            
            if self.debug:
                print(f'pair {pairs}: {pair}')

        print(f'Total pairs: {pairs}')
