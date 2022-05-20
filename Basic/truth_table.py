import itertools
from itertools import product

def truth_table(n):
    iter = product('10', repeat=n)
    for line in iter:
        print(line)
    
n = input("enter a number exponential to the truth table:")  
truth_table(int(n))
