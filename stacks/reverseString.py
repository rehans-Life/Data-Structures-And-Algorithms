def reverseString(s: set):
    
    stack = list()
    ans = ''
    
    for char in s:
        stack.append(char)
        
    for _ in range(len(stack)):
        ans+=stack.pop()
        
    return ans

print(reverseString('abcde'))