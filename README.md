# aoc2022

This has my solutions to the [Advent of Code Challenge](https://adventofcode.com/) in 2022.  No idea if I'll make it to the end (I haven't come close in previous years!)

Run via CLI:

```
usage: aoc2022.py [-h] [-d] [-s] [-v] [--all] day part

positional arguments:
  day              The Day we want to process
  part             Which part we're using

optional arguments:
  -h, --help       show this help message and exit
  -d, --debug      Will create some extra output to add to the confusion. Will also run using the debug data instead of the user data
  -s, --sub        Prints the sub
  -v, --visualise  Displays an visualisations generated for this solution
  --all            Runs all of the solutions! You still need to set the day and part, because I haven't worked out how to make these args optional
```


For example the following will run Day 5, Part 1 with visualisations displayed:

```
python3 aoc2022.py 5 1 -v
```