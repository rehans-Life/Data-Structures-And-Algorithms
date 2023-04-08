def findSuc(root,suc,key):
    
    node = root
    
    while node:
        if node.key > key:
            suc[0] = node
            node = node.left
        else:
            node = node.right
    

def findPre(root,pre,key):
    
    node = root
    
    while node:
        if node.key >= key:
            node = node.left
        else:
            pre[0] = node
            node = node.right
            

def findPreSuc(root, pre, suc, key):
    
    findSuc(root,suc,key)
    findPre(root,pre,key)