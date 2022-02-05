"""
*   @class Stack type
* * there are some useful functions for Stack type, 
* * @func:
* * isEmpty(): if the length of Stack equal 0, 
* *            then return False, otherwise, return True
* * push(data): this func will append the data item into Stack,
* *            it will not return any val
* * peek(): return the top value of Stack
* * size(): return the length of Stack
* * pop(): delete the pop of Stack and return the top value
* * ?examples:
* * my_stack = Stack() / init a empty Stack []
* * my_stack.push('Jax') / ['Jax']
* * my_stack.size() / return 1
* * my_stack.push('Yeah') / ['Jax', 'Yeah']
* * my_stack.peek() / return 'Yeah', and stack is not 
* *                   change ['Jax', 'Yeah']
* * my_stack.pop() / return 'Yeah', and delete 
* *                the top value of stack , ['Jax']
"""

class Stack:   
    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        return not bool(len(self.list))

    def push(self, data):
        self.list.append(data)

    def peek(self):
        return self.list[len(self.list) - 1]

    def size(self):
        return len(self.list)

    def pop(self):
        return self.list.pop()



