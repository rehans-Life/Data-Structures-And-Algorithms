# Unique Subsets of an array

# The situation to apply this occurs when you 
# actually get given an array which has repeating
# elements inside of it.

# Like for example your input is [2,3,3].

# Then here your subsets would be :

# [2,3,3],[2,3],[2,3],[2],[3],[3],[]

# In here we have repeating subsets, like 
# [2,3] and [3] are repeating although there
# formed with different elements but there
# still repeating.

# So we wanna be able to avoid showing these
# repetetive subsets in our power set.

def subsets(array):
    
    # Base Case
    if len(array) == 1:      # ['a'] => [{'a'},{}]
        return [set(array),set()]
    
    powersetOfSlicedArray = subsets(array[1:])

    powersetCopy = [subset.copy() for subset in powersetOfSlicedArray]

    for subset in powersetCopy:
        subset.add(array[0])
    
    powerset = []

    for i in range(len(powersetCopy)):

        if powersetCopy[i] not in powerset:
            powerset.append(powersetCopy[i])
        
        if powersetOfSlicedArray[i] not in powerset:
            powerset.append(powersetOfSlicedArray[i])

    return powerset

# print(subsets(['1','2','2','3']))

def subsetsII(array,i=None,subsets=[],ans=[]):

    array.sort()

    if i == None:
        i=0

    if i == len(array):
        ans.append(subsets.copy())
        return
        
    subsets.append(array[i])
    subsetsII(array,i+1,subsets,ans)

    subsets.pop()

    while i+1 < len(array) and array[i] == array[1+i]:
        i+=1  

    subsetsII(array,i+1,subsets,ans)

    return ans

# print(subsetsII(['a','b','a']))

def uniqueSubsets(array,subset=[],ans=[]):
    
    if len(array) == 0:
        ans.append(subset.copy())
        return
    
    subset.append(array[0])
    uniqueSubsets(array[1:],subset,ans)    

    subset.pop()
    uniqueSubsets(list(filter(lambda x: x != array[0],array)),subset,ans)

    return ans
    
print(uniqueSubsets(['a','b','b']))

