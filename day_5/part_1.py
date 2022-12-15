import shared
from shared import bcolours
from shared import baseSolution
import re

class Solution(baseSolution):
    MOVE = 0
    FROM = 1
    TO = 2

    def get_start_warehouse(self):
        

        if (self.debug):
            warehouse = [
                ['Z','N'],
                ['M','C','D'],
                ['P']
            ]

        else:
            warehouse = [
                ['Z','J','N','W','P','S'],
                ['G','S','T'],
                ['V','Q','R','L','H'],
                ['V','S','T','D'],
                ['Q','Z','T','D','B','M','J'],
                ['M','W','T','J','D','C','Z','L'],
                ['L','P','M','W','G','T','J'],
                ['N','G','M','T','B','F','Q','H'],
                ['R','D','G','C','P','B','Q','W']
            ]

        return warehouse

    def print_crate(self, code):
        print(code,end='')

    def apply_instruction(self, instruction, warehouse):
        num_moves = instruction[self.MOVE] + 1
        move_from = instruction[self.FROM] - 1
        move_to = instruction[self.TO] - 1
        
        for i in range(1, num_moves):
            crate = warehouse[move_from].pop()
            if self.debug:
                print(f'pop {move_from}: {crate} to: {move_to}')
            warehouse[move_to].append(crate)
            i += 1

        return warehouse


    def split_instruction(self, instruction):
        # sample move 1 from 3 to 5
        if self.debug:
            print(instruction)
        return [int(s) for s in re.findall(r'\b\d+\b', instruction)]

    def display_warehouse(self, warehouse):
        sc = 0
        for stack in warehouse:
            sc += 1
            print(f'{sc}:', end='')
            for crate in stack:
                self.print_crate(crate)
            print('')


    def run(self):
        """all the elven magic happens here
        """
        moves = 0

        move_data = shared.fileToArray('day_5/'+self.inputFile)

        warehouse = self.get_start_warehouse()

        print('Start Warehouse:')
        self.display_warehouse(warehouse)

        for move in move_data:
            moves += 1
            self.apply_instruction(self.split_instruction(move), warehouse)
            if self.visualise:
                print(f'\nAfter move {moves}:')
                self.display_warehouse(warehouse)
                print('')
            

        print('Final Warehouse:')
        self.display_warehouse(warehouse)

        print(f'Total moves: {moves}')
