def sumEqualToK(arr,k):
    ans = set()
    def helper(i=0,subset=[],subsetSum=0):
        
        if subsetSum == k:
            ans.add(tuple(subset))

        if i == len(arr):
            return

        subset.append(arr[i])
        helper(i+1,subset,subsetSum+arr[i])

        subset.pop()
        helper(i+1,subset,subsetSum)
    helper()
    return sorted(list(ans))

print(sumEqualToK([5, -2, 0, -5, 2],0))