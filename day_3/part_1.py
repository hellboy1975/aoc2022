import shared
import string

class Solution:

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    def get_priority(self, item):
        """uses the position of the letter within the alphabet to determine a priority

        Args:
            item (_type_): the letter of the alphabet for analysis

        Returns:
            integer: the priority
        """
        return string.ascii_letters.index(item) + 1

    def run(self):
        """all the elven magic happens here
        """
        rucksacks = priority_total = 0

        rucksack_data = shared.fileToArray('day_3/'+self.inputFile)

        for contents in rucksack_data:
            compartment_1 = contents[slice(0,len(contents)//2)]
            compartment_2 = contents[slice(len(contents)//2, len(contents))]
            if self.debug:
                print(f'compartment_1: {compartment_1} compartment_2: {compartment_2}')

            # intersect the two arrays and pop the first item out (there should only ever be 1)
            item = set(compartment_1).intersection(compartment_2).pop()
            priority = self.get_priority(item)
            if self.debug:
                print(f'item: {item} | {priority}')

            priority_total += priority
            rucksacks += 1

        print(f'Total rucksacks: {rucksacks}')
        print(f'Total p total: {priority_total}')
