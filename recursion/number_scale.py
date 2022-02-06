##
##

import sys

def numberScale(num, scale):
    dic = "0123456789ABCDEF"
    if (num < scale):
        return dic[num]
    else:
        return numberScale(num //scale, scale) + dic[num % scale]

print(numberScale(8, 2))
print(numberScale(255, 2))

print(sys.getrecursionlimit())

