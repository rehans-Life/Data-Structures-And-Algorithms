def predessesorBST(root,key: int) -> int:
    predessesor = None
    
    while root:
        
        if root.val >= key:
            root = root.left
        else:
            predessesor = root.val
            root = root.right
    
    return predessesor