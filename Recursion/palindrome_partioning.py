def check_palindrome(s,start=None,end=None):
    if start == None:
        start = 0
    
    if end == None:
        end = len(s)-1

    if s[start] != s[end]:
        return False
    
    if start == len(s) // 2 or end == len(s) // 2:
        return True
    
    return check_palindrome(s,start+1,end-1)

def palindrome_partioning(s):
    ans = []
    # Creating a helper function starting with parameter set to 0 by default and a substrings array which consists of all the substrings
    # of the string.
    def helper(i=0,substrings=[]):
        
        # If i reaches the length of the string which means i have divided the whole string into a substring therefore i can append
        # the array containing all the substrings i have divided the string into to into my answers array.
        if i == len(s):
            ans.append(substrings.copy())
            return
        
        for j in range(i,len(s)):
            if check_palindrome(s[i:j+1]):
                substrings.append(s[i:j+1])
                helper(j+1)
                substrings.pop()
    helper()
    return ans    
print(palindrome_partioning('reehhhanffffdssdsdwwwww'))