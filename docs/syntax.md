## Learn syntax in Python
### Variables
First, python has no command for declaring a variable. in Python you can just write the variable name and assign a value to it.
```python
x = 'Jax'
y = 5
```
If you want specify the data type of a variable, you can use the casting feature.
```python
x = str(5) # x = '5'
y = int(5) # y = 5
z = float(5) # z = 5.0
```
Python allows you to assign muilt-variables in one line:
```python
x, y, z = 1, 2, 3
```
### Data Types 
|categories|types|
| ----------- | ----------- |
| Text Type | str|
| Numeric Types | int, float, complex|
|Sequence Types|list, tuple, range|
|Mapping Type|dict|
|Set Types|	set, frozenset|
|Boolean Type|bool|
|Binary Types|bytes, bytearray, memoryview|

```python
x = 'hello world' # str
x = 5 # int
x = 5.0 # float
x = 1j # complex 表示复数，其中j是虚数部分
x = ['a', 'b', 'c'] # list 
x = ('a', 'b', 'c') # tuple
x = range(5) # range [0, 1, 2, 3, 4, 5]
x = {'name' : 'jax', 'age' : '18' } # dict
x = {1 ,2 ,3 ,4} # set 集合的含义
x = frozenset({1 ,2 ,3 ,4}) # frozenset 不可变集合
x = True ｜ False # bool
x = b'hello world' # bytes 
x = bytearray(1) # bytearray
x = memoryview(bytes(5)) # memoryview
```
### Operators
**Arithmetic Operators**
|Operator|Name|
| ----------- | ----------- |
|+|Addition|
|-|Subtration|
|*|Multipication|
|/|Divison|
|%|Modulus|
|**|Exponentiation 乘方|
|//|Floor division|

**Assignment Operators**
* =
* +=
* -=
* /=
* *=
* **=
* %=
* //=
* &=
**Comparison Operators**
* ==
* !=
* >
* <
* >=
* <=
**Logical Operators**
* and
* or 
* not
**Identity Operators**
* is
* is not
**Membership Operators**
* in
* not in

### If statement
```python
if expression:
    XXXXXX
elif expression:
    XXXXXX
else:
    XXXXXX

# 三目表达式
x if expression else expression
# eg:
x = '' if False else 'jax'
```
### For and While
```python
# while
while expression:
    XXXXXX
# eg -> output: 0 1 2 3 4 5
i = 0
while i < 6
    print(i)
    i += 1

# for
for i in object:
    XXXXXX
# eg -> output: 0 1 2 3 4 5
for i in range(6)
    print(i)

# break and continue statement
# break : stop the loop 
# continue : stop the current iteration and go to next
# break eg -> output: 0 1 2 
i = 0
while i < 6:
  if i == 3:
    break
  print(i)
  i += 1
# continue eg -> output: 0 1 2 4 5
i = 0
while i < 6:
  if i == 3:
    continue
  print(i)
  i += 1

# with else statement, when the condition is not true , then run the else statement section 
i = 0
while i < 6:
  print(i)
  i += 1
else:
  print('now i == 6')
```

### Function
```python
def function_name (arg1, arg2 ...):
    XXXXXXX
    XXXXXXX
    return XXXXXX # return statement is optional in one function

# eg -> with no arguments
def func():
    print('please do not pass any arguments')

# eg -> with arugments
def func(arg1):
    print(arg1)
func('hello world')

# set default value to arguments
def func(arg1 = 'hello world')
    print(arg1)
func()
```
### Function Annotation
```python
def add(x:int, y:int) -> int:
    return x + y
```