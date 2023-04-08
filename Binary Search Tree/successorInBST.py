def successorBST(root,x: int) -> int:
        successor = None
        
        while root:
            
            if root.data > x.data:
                successor = root.data
                root = root.left
                
            else:
                root = root.right
                
        return successor