def longestKSubstr(s, k):
        n = len(s)
        # Two pointers to create windows in which we can check our
        # answers inside of.
        i,j=0,0
        
        # Maintianing a Map to store the number of unique characters
        # in a hashmap
        unique = dict()
        
        # A count variable which is going to store the number of unique
        # characters inside of a substring
        count = 0
        
        # A variable which is going to store the length of the longest
        # subarray at different intervals.
        maxSubstring = -1
        
        while j < n:
            
            # The calculation in this sliding window question is that
            # we keep adding elements that j pointer is traversing 
            # through to the hashmap.
            
            # If the character j pointer is traversing isnt already
            # in the hashmap then that means this is a unique 
            # character that we have found so we add it to the hashmap
            # and increment count.
            
            if s[j] not in unique:
                unique[s[j]] = 1
            else:
                unique[s[j]]+=1    
            
            # We incrementing j until we hit the condition
            if len(unique) < k:
                j+=1
            elif len(unique) == k:
                # Once we find a substring with equal number of unique
                # characters to k i check if its length is greater than
                # the previous substring i found which had k number of
                # unique characters.
                maxSubstring = max(maxSubstring,j-i+1)
                j+=1
            elif len(unique) > k:
                # When number of unique characters is greater i keep
                # incrementing i and remove the characters from the 
                # hashmap and i try to bring the number of unique
                # characters back to being less than or equal to 
                # k
                while len(unique) > k:
                    if unique[s[i]] == 1:
                        del unique[s[i]]
                    else:
                         unique[s[i]]-=1                        
                    i+=1
                j+=1
            
        return maxSubstring

print(longestKSubstr('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco',5))