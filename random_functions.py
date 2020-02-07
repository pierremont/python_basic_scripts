

# seed the pseudorandom number generator
from random import seed
#from random import random
from random import randint #integer numbers

# seed random number generator
seed()
# generate some random numbers
#print(random(), random(), random())
# reset the seed

for x in range (9):
    for y in range(9):
        print (randint(0,10), end = ", ")
    print()

