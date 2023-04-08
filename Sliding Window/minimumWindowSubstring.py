from math import inf
def minWindowSubStr(s: str,t: str):
    
    n = len(s)
    
    # Initializing two pointers at the start and at the end of our window.
    i,j=0,0
    
    # Maintaining a hashmap for storing the characters and there frequencies 
    # which are inside of our string t.
    dic = dict()
    
    for char in t:
        if char not in dic:
            dic[char] = 0
        dic[char]+=1
    
    
    # This count variable is going to maintain the count as to how many characters does our currrent
    # substring does not have in equal frequency to given string 't'. 
    count = len(dic)
    
    print(count)

    
    # A variable to store the smallest substring length.
    minWindowLength = inf
    
    while j < n:
        
        # We will check if the element through our j pointer is traversing through is inside of our
        # hashmap then we decrement cause thats going to denote that we have found an element in our
        # substring that present inside of our string 't'.
        if s[j] in dic:
            dic[s[j]]-=1
            # Also if its count has gone to zero that means the frequency of this element inside of our
            # current subStr is equivalent to its frequency in our string t so we decrement count as 
            # denoting that there is one less element which does not exist in equal to our string 't'.
            if dic[s[j]] == 0:
                count-=1
        
        # If count is zero then that means our current substring has all the elements of our string t
        # and it includes them in equal frequencies therefore this is a candidate for our answer.
        if count == 0:
            # We keep moving our ith element as long as count is zero so we are basically shrinking our 
            # window cause that can be a better answer than the current one we have found.
            while count == 0:
                minWindowLength = min(minWindowLength,(j-i+1))
                # We undoing the calculations for our ith element because its not going to be inside of
                # our new window.
                if s[i] in dic:
                    dic[s[i]]+=1
                    # If the count goes to one from zero than that means that this element does not 
                    # exists in equal frequency to our string t so we incremeent count.
                    if dic[s[i]] == 1:
                        count+=1
                i+=1
            j+=1
        elif count > 0:
            # We keep moving jth element until we find a substring with all these characters. 
            j+=1
    
    return minWindowLength

print(minWindowSubStr('totmtaptat','tta'))