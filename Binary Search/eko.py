def atleastMWood(trees,n,m,height):
    woodsCollection = 0
    for tree in trees:
        woodsCut  = tree-height
        if (woodsCut) > 0:
            woodsCollection+=woodsCut
        if woodsCollection >= m:
            return True
    return False

def eko(trees,n,m):
    
    start = 0
    end = max(trees)
    res = -1
    
    while start <= end:
        mid = (start+end) // 2
        if atleastMWood(trees,n,m,mid):
            res = mid
            start = mid+1
        else:
            end = mid-1
    return res    