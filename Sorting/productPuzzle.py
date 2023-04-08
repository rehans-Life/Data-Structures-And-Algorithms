# Brute Force

# Time Complexity: O(n)
# Space Complexity: O(n)

def productPuzzle(arr,n):
    
    prefix = [0] * n
    postFix = [0] * n
    answers = [0] * n
    
    prefixProduct = 1
    postProduct = 1
    
    for i in range(n):
        prefixProduct*=arr[i]
        prefix[i] = prefixProduct
    
    for j in reversed(range(n)):
        postProduct*=arr[j]
        postFix[j] = postProduct
    
    for z in range(n):
        
        startToPrev = prefix[z-1] if z-1 >= 0 else 1
        frontToEnd = postFix[z+1] if z+1 < n else 1
        
        answers[z] = startToPrev * frontToEnd
    
    return answers

arr = [5,8,2,4,3]
n = len(arr)

print(productPuzzle(arr,n))

# Optimal 

# Time Complexity: O(n)
# Space Complexity: O(1) // Not counting the answers array

def productPuzzleII(arr,n):
    
    answers = [0] * n
    
    prefixProduct = 1
    
    # 1st Pass to store the prefix products which is the product of elements from the start till the element right behind our current
    # element.
    for i in range(n):
        answers[i] = prefixProduct
        prefixProduct*=arr[i]
        
    postfixProduct = 1
    
    # 2nd Pass to multiply the post products into the prefix products which is basically the product of the element from the end till the
    # element right infront on our current element
    for j in reversed(range(n)):
        answers[j] = answers[j] * postfixProduct
        postProduct*=arr[i]
    
    return answers

print(productPuzzle(arr,n))