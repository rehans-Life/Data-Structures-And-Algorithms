def printSeries(n, k):
    # Write your code here
    series=[]
    def helper(n,k,diff,i=0):
        series.insert(i,diff)
        if diff <= 0:
            return
        series.insert(i,diff) 
        helper(n,k,diff-k,i+1)
    helper(n,k,n)
    return series
# print(printSeries(5,3))

def printSeriesII(n,k):
    series=[]
    def helper(n,k,currNum=n,flag=0):
        if flag == 2:
            return
        series.append(currNum)
        if flag == 0:
            if currNum >= 0:
                helper(n,k,currNum-k,0)
            else:
                helper(n,k,currNum+k,1)
        if flag == 1:
            if currNum < n:
                helper(n,k,currNum+k,1)
            elif currNum == n:
                helper(n,k,currNum+k,2)
    helper(n,k)
    return series
# print(printSeriesII(5,2))
print('25'.find('5'))
