from math import remainder
from . import Stack

def divideBy2(num):
    remainder = 1
    remStack = Stack.Stack() # rem means remainder
    binString = "" # bin means binary
    signum = ""

    if num < 0:
        signum = "-" 
    num = abs(num)

    while(num > 0):
        remainder = num % 2
        remStack.push(remainder)
        num = num // 2

    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())

    if binString == "":
        binString = binString + "0"

    return signum + binString