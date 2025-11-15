#import library name

# this import all functions from the library

import random

#libraryName.FunctionName
print(random.randint(1,10)) # returns a random value within the range inclusive

# from libraryName import FunctionName

from random import randint
print(randint(1,10))