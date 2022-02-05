import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from stack.Stack import Stack
from stack.parChecker import parChecker, muiltParChecker
from stack.divideBy2 import divideBy2

# ** define a Stack Object
my_stack = Stack()

# ** test push func
def test_stack_push():
    my_stack.push('Jax')
    assert my_stack.list[len(my_stack.list) - 1] == 'Jax'
    my_stack.push(0)
    assert my_stack.list[len(my_stack.list) - 1] == 0

# ** test isEmpty func
def test_stack_isEmpty():
    assert my_stack.isEmpty() == False

# ** test parChecker func
def test_parChecker():
    assert parChecker("()") == True
    assert parChecker("(()") == False
    assert parChecker("()()") == True
    assert parChecker("())") == False
    assert parChecker("((()))") == True


# ** test muiltParChecker func
def test_muiltParChecker():
    assert muiltParChecker("()") == True
    assert muiltParChecker("(()") == False
    assert muiltParChecker("()()") == True
    assert muiltParChecker("())") == False
    assert muiltParChecker("((()))") == True

    assert muiltParChecker("{{[()]}}") == True
    assert muiltParChecker("{}()[]") == True
    assert muiltParChecker("()[)") == False
    assert muiltParChecker("{{}") == False
    assert muiltParChecker("((()])") == False

# ** test divideBy2 func
def test_divideBy2():
    assert divideBy2(0) == "0"
    assert divideBy2(1) == "1"
    assert divideBy2(2) == "10"
    assert divideBy2(8) == "1000"
    assert divideBy2(100) == "1100100"
    assert divideBy2(255) == "11111111"

    assert divideBy2(-1) == "-1"
    assert divideBy2(-2) == "-10"
    assert divideBy2(-8) == "-1000"
    assert divideBy2(-100) == "-1100100"
    assert divideBy2(-255) == "-11111111"