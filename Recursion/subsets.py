# Find all the possible subsets of an array.

# For Example [a,b,c]: 

# Subsets : {(),(a),(b),(c),(a,b),(b,c),(a,c),(a,b,c)}

def subsets(array):
    
    if len(array) == 0:
        return [set()]
    
     
    powersetOfSlicedArray = subsets(array[1:])

    powersetCopy = [subset.copy() for subset in powersetOfSlicedArray]

    for subset in powersetCopy:
        subset.add(array[0])
    
    powerset = powersetOfSlicedArray + powersetCopy

    return powerset

# print(subsets(['a','b','c']))

def subsetsII(array,i=0):

    if i == len(array):
        return [set()]
    
    powersetSlicedArray = subsetsII(array,i+1)

    powersetCopy = [subset.copy() for subset in powersetSlicedArray]

    for subset in powersetCopy:
        subset.add(array[i])
    
    return powersetSlicedArray + powersetCopy

# print(subsetsII(['a','b','c']))

def mySubsetsII(array,subset=[],ans=[]):

    array.sort()

    if len(array) == 0:
        ans.append(subset.copy())
        return
    
    subset.append(array[0])
    mySubsetsII(array[1:],subset,ans)    

    subset.pop()
    mySubsetsII(array[1:],subset,ans)

    return ans
print(mySubsetsII(['a','c','a']))