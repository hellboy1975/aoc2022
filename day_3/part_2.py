import string
import shared
from shared import baseSolution

class Solution(baseSolution):
    """ Solution for Day 3 Part 2
    """

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
        group = []

        rucksack_data = shared.fileToArray('day_3/'+self.input_file)

        for contents in rucksack_data:
            rucksacks += 1

            # if we keep on intersecting, by the time we get to round 3 there should be only one
            if not group:
                group = set(contents)
            else:
                group = set(contents).intersection(group)

            if rucksacks % 3 == 0:
                item = group.pop()

                priority = self.get_priority(item)
                if self.debug:
                    print(f'item: {item} | {priority}')

                group = []
                priority_total += priority

        print(f'Total rucksacks: {rucksacks}')
        print(f'Total p total: {priority_total}')
