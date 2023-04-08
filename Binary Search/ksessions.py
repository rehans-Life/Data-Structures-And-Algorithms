t = int(input())

def check(sessions,k,d):
    no_of_insertions = 0
    for i in range(len(sessions)-1):
        if (sessions[i+1] - sessions[i]) > d:
            no_of_insertions+=((sessions[i+1]-sessions[i]-1)//d)
            if no_of_insertions > k:
                return False
    return True

tc = 1
while t > 0:
    
    n,k = map(int,input().split())
    sessions = list(map(int,input().split()))
    
    start = 1
    end = 1e9
    res = -1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        if check(sessions,k,mid):
            res = mid
            end = mid-1
        else:
            start = mid+1
    
    print(f"Case #{tc}: {int(res)}")
    tc+=1
    t-=1
    