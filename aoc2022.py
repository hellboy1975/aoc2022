import argparse
import shared
from shared import bcolours

parser = argparse.ArgumentParser()
parser.add_argument("day",help = "The Day we want to process", type=int)
parser.add_argument("part",help = "Which part we're using", type=int)
parser.add_argument("-d", "--debug",help = "Will create some extra output to add to the confusion.  Will also run using the debug data instead of the user data", action="store_true")
parser.add_argument("-s", "--sub",help = "Prints the sub", action="store_true")
parser.add_argument("-v", "--visualise",help = "Displays an visualisations generated for this solution", action="store_true")
parser.add_argument("--all",help = "Runs all of the solutions!  You still need to set the day and part, because I haven't worked out how to make these args optional", action="store_true")

args = parser.parse_args()

# this should really only ever be 1 or 2 - if it's not 2, make it one!
if args.part != 2:
    args.part = 1

debug = args.debug
if debug:
    print('  Debug on!')

solutions_list = shared.getSolutions()

if args.sub:
    shared.printSubmarine()

if args.all:
    print(f'{bcolours.BLUEBG}Running all possible solutions!{bcolours.ENDC}')    
    for s in solutions_list:
        print(f'Processing AOC2022 {bcolours.OKBLUE} {s} {bcolours.ENDC}')
        shared.runSolution(s, debug, args.visualise)

else:
    solution = f'day_{args.day}.part_{args.part}'
    print(f'Processing AOC2021 {bcolours.OKBLUE} Day: {args.day} Part: {args.part}{bcolours.ENDC}')
    if solution not in solutions_list:
        print(f'{bcolours.WARNING}This challenge hasn\'t been attempted yet.  Maybe some day....{bcolours.ENDC}')    
        exit()
    shared.runSolution(solution, debug, args.visualise)
