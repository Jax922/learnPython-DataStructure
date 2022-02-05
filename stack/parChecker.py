# **  

from . import Stack

def parChecker(symbolString):
    stack = Stack.Stack()
    for item in range(len(symbolString)):
        symbol = symbolString[item]
        if symbol == "(":
            stack.push(symbol)
        elif symbol == ")":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    return stack.isEmpty()

def matcher(start, end):
    starts = "([{"
    ends = ")]}"
    return starts.index(start) == ends.index(end)

def muiltParChecker(symbolString):
    stack = Stack.Stack()
    for item in range(len(symbolString)):
        symbol = symbolString[item]
        if symbol in "([{": 
            stack.push(symbol)
        elif symbol in ")]}":
            if not stack.isEmpty() and matcher(stack.peek(), symbol):
                stack.pop()
            else:
                return False
    return stack.isEmpty()



