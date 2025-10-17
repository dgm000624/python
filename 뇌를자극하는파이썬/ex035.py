def maxTwo(i,j):
    if i > j: return i
    else : return j

def maxThree(x,y,z) :
    return maxTwo(maxTwo(x,y), maxTwo(y,z))

maxnum = maxThree(3,9,5)

print(maxnum)