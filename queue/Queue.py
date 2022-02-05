""" 
* * Class Queue
* * @func inqueue(): append a value into last of the queue and return None
* * @func dequeue(): delete the front of the queue and return it 
* * @func isEmpty(): if the queue is [], then return True, else return False
* * @func size(): return the length of the queue
"""
from typing import Any

class Queue:
    def __init__(self):
        self._queue = []

    def inqueue(self, val: Any):
        self._queue.append(val)
        return None
    
    def dequeue(self) -> Any:
        if self._queue == []:
            return None
        else: 
            temp = self._queue[0]
            del self._queue[0]
            return temp
    
    def isEmpty(self) -> bool:
        return self._queue ==[]
    
    def size(self) -> int:
        return len(self._queue)



