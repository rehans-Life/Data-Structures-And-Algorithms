# All the permutations of an array.

def permutations(array):

    if len(array) == 2:
        return [[array[0],array[1]],[array[1],array[0]]]
    
    permutationsArray = []
 
    for item in array:

        arrayCopy = array.copy()
        arrayCopy.remove(item)

        permutationsSubArray = permutations(arrayCopy)

        for permutation in permutationsSubArray:
            permutation.insert(0,item)

        permutationsArray.extend(permutationsSubArray) 
    
    return permutationsArray

# print(permutations([1,2,3,4]))

def myPermutations(array):

    if len(array) == 2:
        return [[array[0],array[1]],[array[1],array[0]]]
    
    permutationsArray = []

    inserts = [0,len(array)//2,len(array) - 1]

    for i in range(len(inserts)):
        permutationsSubArray = permutations(array[1:])

        for permutation in permutationsSubArray:
            permutation.insert(inserts[i],array[0])

        permutationsArray.extend(permutationsSubArray)
    
    return permutationsArray

# print(myPermutations([2,3,4]))

def uniquePermutations(string):

    if len(string) == 2:
        return [string,string[1]+string[0]]

    permutationsArray = []

    for character in string:

        stringCopy = list(string)
        stringCopy.remove(character)

        permutationsSubArray = uniquePermutations(''.join(stringCopy))

        for permutation in permutationsSubArray:
            permutation = character + permutation
            # We just make sure that the permutation were going to add is not 
            # already in the array
            if permutation not in permutationsArray:
                permutationsArray.append(permutation)
        
    return permutationsArray

print(uniquePermutations('hamad'))