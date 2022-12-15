import shared
from shared import bcolours

class Solution:

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    def get_start_warehouse(self):
        

        if (self.debug):
            warehouse = {
                "1": ['Z','N'],
                "2": ['M','C','D'],
                "3": ['P']
            }

        else:
            warehouse = {
                "1": ['Z','J','N','W','P','S'],
                "2": ['G','S','T'],
                "3": ['V','Q','R','L','H'],
                "4": ['V','S','T','D'],
                "5": ['Q','Z','T','D','B','M','J'],
                "6": ['M','W','T','J','D','C','Z','L'],
                "7": ['L','P','M','W','G','T','J'],
                "8": ['N','G','M','T','B','F','Q','H'],
                "9": ['R','D','G','C','P','B','Q','W']
            }

        return warehouse

    def print_crate(self, code):
        print(code,end='')

    def display_warehouse(self, warehouse):
        print(warehouse)
        sc = 0
        for stack in warehouse:
            sc += 1
            print(stack)
            # print(f'{sc}:', end='')
            for crate in stack:
                print(crate)
                # self.print_crate(crate)
            # print('')


    def run(self):
        """all the elven magic happens here
        """
        moves = 0

        move_data = shared.fileToArray('day_5/'+self.inputFile)

        warehouse = self.get_start_warehouse()

        self.display_warehouse(warehouse)

        for move in move_data:
            moves += 1


        print(f'Total moves: {moves}')
