## Learn data structure by Python

- [Learn data structure by Python](#learn-data-structure-by-python)
  - [Complexity:Big O](#complexitybig-o)
  - [Linear Structure](#linear-structure)
    - [Stack](#stack)
    - [Queue](#queue)
    - [List](#list)
  - [Recursion](#recursion)


### Complexity:Big O
大O表示法：一段代码中赋值语句执行次数的主要影响因子，一般记为O(n);
比如一般代码的赋值语句执行了2n+69次，那么O(n)=n
```python
# eg: O(1)
def complex_O1():
    x = 1
    y = 2
    return x + y
# eg: O(n)
def complex_On():
    x = 5
    sum = 0
    for i range(x):
        sum += i
    return sum
# eg: O(n^2)
def complex_On2():
    x = 5
    y = 10
    sum = 0
    for i range(x):
        for j range(y):
            sum = sum + (i * j)
    return sum

# eg: O(logn)
# 赋值语句会执行 log(n)+1次，底为2
def complex_Ologn(n):
    i = 1
    while i > n:
        i *= 2

```

### Linear Structure
#### Stack
> LIFO：Last in First out
> 有次序的数据项集合，在栈中，数据项的加入和移除都仅发生在同一端

基于Python的代码实现如下：
```python
class Stack:   
    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        return not bool(len(self.list))

    def push(self, data):
        self.list.append(data)

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def pop(self):
        return self.list.pop()

```

#### Queue
> 有次序的数据集合，添加发生在一端，删除必须在另一端；即一个入口，一个出口
> FIFO：First-in-first-out

```python
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
```

#### List
> 【无序列表】：
> Python已经实现了List数据类型，同时配套了很强大数据操作函数;相当于其他语言中的Array Object

* insert(index, value)
* append(value)
* extend(otherList)
* remove(value)
* pop(index),index is optional
* sort() 
* sort(reverse = True)
* sort(key = func_name) customize the list by your function
* sort(key = str.lower) 
* reverse()
* copy()
* list1 + list2 the puls operator can use to join the two lists 
* count(value) return the number of element
* clear() remove all elements


```python
# 在python中声明一个List很简单：
list1 = []
list2 = [1, 2, 3]
list3 = [1, 2, 'jax', 'hello world']
#或者使用list()函数声明一个list
list4 = list(('a', 'b', 'c'))

#访问list中的item：
list1[0]
```

>【无序列表】：除了Array类型外，单向链表也算一种无序列表：
* add
* size
* search(value)
* remove(value)
* append(value)
* pop(index) index is optional

待用python实现

>【有序列表】：在Array特效下需要保持个数据项之间的顺序

eg:[1, 2, 3, 4, ...]


### Recursion
>递归将大规模问题分解成更小的相同问题，这是一种解决问题的思路

eg: 数列求和问题
```python
list1 = [1,2,3,4]

#遍历list求和
sum = 0
for item in list1:
    sum += item

#递归思路解法：将求和问题拆解成两部分，
# sum(list1) = list1[0] + sum(list1[1:])
# 1+[2,3,4] -> 1 + 2 +[3,4] -> 1 + 2 + 3 +[4]
def recurisonSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + recurisonSum(numList[1:])

```
- 递归算法必须有一个基本结束条件，也就是最小规模的解决方案
- 递归算法必须能改变状态向基本结束条件逼近
- 递归算法必须是调用自身，其实也是一种循环





