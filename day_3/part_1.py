import shared

class Solution:

    

    def __init__(self, debug):
        self.debug = debug

        self.inputFile = 'data.txt'
        if (debug):
            self.inputFile = 'debug_data.txt'

    def addItem(cls, item, itemDictionary):
        
        if not item in itemDictionary:
            itemDictionary[item] = 1
        else:
            itemDictionary[item] += 1

        return itemDictionary


    def run(self):
        rucksacks = 0
        itemDictionary = {}

        rucksackData = shared.fileToArray('day_3/'+self.inputFile)

        for x in rucksackData:
            c1 = x[slice(0,len(x)//2)]
            c2 = x[slice(len(x)//2, len(x))]
            if (self.debug):
                print(f'c1: {c1} c2: {c2}')

            item = set(c1).intersection(c2)
            if (self.debug):
                print(f'item: {item}')

            self.addItem(item=item, itemDictionary=itemDictionary)

            rucksacks += 1
                
        print(f'Total rucksacks: {rucksacks}')     