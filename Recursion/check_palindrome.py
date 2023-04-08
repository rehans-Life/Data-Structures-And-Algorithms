# Check weather a string is palindrome or not 

# A Palindrome is a word which is equal to its reverse.

def check_palindrome(word,left=None,right=None):
    if left == None:
        left = 0
    
    if right == None:
        right = len(word) - 1 

    if word[left] != word[right]:
        return False
    
    if left == (len(word) // 2) or right == (len(word) // 2):
        return True

    return check_palindrome(word,left + 1,right - 1)

print(check_palindrome('abceecba'))