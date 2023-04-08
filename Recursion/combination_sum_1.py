# Combination Sum

# I will follow the pointer approach in order to solve this,
# In which you have a pointer pointing towards the value
# in the array which you want to include in the subsets
# of the remaining array and not include in the other set
# And you also make sure your incrementing the pointer
# upon each recursion call that you make to the point 
# towards the next item in the array.

# In combination sum - within which we have to find all
# combinations of a given sum.
  
# we will be using the same technique but in this 
# combination sum approach we can repeat elements as many 
# times as we want to so we have to upgrade this technique 
# in a way that helps us meet our requirements for the
# question.

# The way we have to upgrade this approach is that when
# we include the element to which our pointer is pointing
# to in the array in that case we dont increment the pointer
# to point towards the next element in the array why because
# we would need to make use of that element again in the
# future in order to get the combinations with the element
# within.

# And also even if we dont increment i now then in the future
# we will again have the option to increment i again

# But if we increment the pointer now then i loose it 
# forever and i dont want that to happen since I would need
# it in the future but even if i dont increment the counter
# i will still have the option in the future to not increment
# it.
 
# But when we ignore here we would increment the 
# pointer why because since we are ignoring the element
# that means there is no way we are going to use that 
# element in the future so then we point towards the next
# element in the array.

# Lets also draw the recursion and find out at what conditions
# do we need to stop the recursive calling of functions
# So we identify the base cases here.

def combinationSum(array,k,i=0,combination=[],ans=[]):

    if i == len(array):
        return
    
    if sum(combination) == k:
        ans.append(combination.copy())
        return
    
    if sum(combination) > k:
        return
    
    combination.append(array[i])
    combinationSum(array,k,i,combination,ans)

    combination.pop()
    combinationSum(array,k,i+1,combination,ans)

    return ans

print(combinationSum([1,2,3],5))