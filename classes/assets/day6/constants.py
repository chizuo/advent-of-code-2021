# Constants for Lantern Fish problem, day 6
# Required since algorithm used is based on assumptions that these values do not change

# days required for a lanternfish to give birth and return back to its original starting number
daysPerCycle = 7

# dictionary that maps starting number of new lanternfish after a cycle (7 days)
# based on the parent's starting number. This will change based on observationLength, daysPerCycle, and range of numbers
mapping = {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 0, 8: 1}
