##

def recurisonSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + recurisonSum(numList[1:])



print(recurisonSum([1,2,3,4]))