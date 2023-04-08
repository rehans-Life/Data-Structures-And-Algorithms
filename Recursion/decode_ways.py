nums=0
def helper(s,i):
            global nums
        # If i is equal to the length that means i have generated a valid combinations from 
        # the integers that i decode into a string.
            if i >= len(s):
        # Thats why im incrementing ways cause i have found a way to decode the nums string
        # into a valid string.
               nums+=1
               return
            # Cause if i try to create any combinations in which zero exists individually
            # or if i try to generate any combination in which i have a pair where zero
            # exists infront of the integer.
            if s[i] == '0':
                return
            
            helper(s,i+1)

            # When to take pairs.

            if  i+1 < len(s) and int(s[i]+s[i+1]) <= 26:
                helper(s,i+2)
            
def numDecodings(s):
       global nums
       helper(s,0)
       return nums
# print(numDecodings("1111111"))

arr=[1,2,3,4,5,6,7]
print(sum(arr[0:4]))