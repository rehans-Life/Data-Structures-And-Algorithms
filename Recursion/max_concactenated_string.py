# Finding and Returning the length of the longest concactenated string.

def maxConcactenatedString(arr):
    used = [0] * 26 
    def helper(arr,i=0,length=0):
        
        if i == len(arr):
            return length
        
        repeating = False

        for letter in arr[i]:
            letterIndex = ord(letter) - ord('a')
            if used[letterIndex] == 1:
                repeating=True
            elif arr[i].count(letter) > 1:
                repeating = True

        if not repeating:
            for letter in arr[i]:
                letterIndex = ord(letter) - ord('a')
                if used[letterIndex] == 0:
                    used[letterIndex] = 1

            maxLength1 = helper(arr,i+1,length + len(arr[i]))

            for letter in arr[i]:
                letterIndex = ord(letter) - ord('a')
                used[letterIndex] = 0

            maxLength2 = helper(arr,i+1,length)
            return maxLength1 if maxLength1 > maxLength2 else maxLength2
        else:
            return helper(arr,i+1,length)

    return helper(arr)
print(maxConcactenatedString(['ccca','ewrghbnmkliop','fgvcxz']))