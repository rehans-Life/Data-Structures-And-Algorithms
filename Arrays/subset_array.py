# Space COmplexity: O(n)
# Time Complexity: O(n+m)

def isSubset( a1, a2, n, m):
    freq = dict()
    
    for num in a1:
        if num in freq:
            freq[num]+=1
        else:
            freq[num] = 1
    
    for num in a2:
        if num in freq:
            if freq[num] > 0:
                freq[num]-=1
            else:
                return 'No'
        else:
            return 'No'
    
    return 'Yes'