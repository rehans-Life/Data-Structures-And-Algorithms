# First Approach I

letters = {
        '1':[],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }

def combinationsI(s):
    global letters
    # Write your code here

    def helper(s,i=0):
        
        if i==len(s):
            return [str()]
        
        combinationsSubString = helper(s,i+1)

        combinations = []
        
        for letter in letters[s[i]]:
            for combination in combinationsSubString:
                combinations.append(letter + combination)

        return combinations 

    return helper(s)
combinationsI('658')

def combinationsII(s,i=0,combination=[],ans=[]):
    
    global letters

    # If i is equal to length then that means i have generated
    # a valid combination and we add it to the ans
    if i == len(s):
        ans.append(''.join(combination))
        return

    # Iterating through each letter to which my ith element
    # represents 
       
    for letter in letters[s[i]]:

        # Adding that letter to our combination
        combination.append(letter)

        # Creating combinations starting from element one index
        # ahead of our ith element till the end and all those 
        # combinations will have the letter of current iteration
        # within them
        combinationsII(s,i+1,combination,ans)

        # Backtracking and removing the letter that we added
        # earlier because we have already generated all possible
        # combinations with it.
        combination.pop()
    return sorted(ans)                         

print(combinationsII('2345'))