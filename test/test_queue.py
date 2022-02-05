import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from queue.Queue import Queue

# ** define a Queue Object
my_queue = Queue()
my_queue.inqueue('Jax')
my_queue.inqueue('Jax-1')
# ** test inqueue func
def test_queue_inqueue():
    assert my_queue._queue[len(my_queue._queue) - 1] == 'Jax-1'

# ** test inqueue func
def test_queue_dequeue():
    assert my_queue.dequeue() == 'Jax'
    assert my_queue.dequeue() == 'Jax-1'
    my_queue.inqueue(1)
    my_queue.inqueue(2)
    assert my_queue.dequeue() == 0
    assert my_queue.dequeue() == 1

# # ** test isEmpty func
def test_queue_isEmpty():
    temp_queue = Queue()
    assert temp_queue.isEmpty() == True
    temp_queue.inqueue(0)
    assert temp_queue.isEmpty() == False

# # ** test size func
def test_queue_size():
    temp_queue = Queue()
    temp_queue.inqueue(1)
    temp_queue.inqueue(2)
    assert temp_queue.size() == 2