## Learn data structure by Python
### 计算复杂度
大O表示法：一段代码中赋值语句执行次数的主要影响因子，一般记为O(n);
比如一般代码的赋值语句执行了2n+69次，那么O(n)=n

### Linear Structure
**Stack**
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

**Queue**
> 有次序的数据集合，添加发生在一端，删除必须在另一端；即一个入口，一个出口
> FIFO：First-in-first-out
