from queue import Queue

class Solution:
    # This function checks that if the binary tree follows the max heap
    # order property which states that each node should be greater than
    # both of its children.
    def isHeapOrder(self,root):
        
        if not root:
            return True
        
        leftChild = root.left
        rightChild = root.right
        
        # If the root is not greater than both of its children then i 
        # return False cause then the binary tree doesnt follow the 
        # heap order property.
        if (leftChild and leftChild.data > root.data) or (rightChild and rightChild.data > root.data):
            return False
            
        # Then I make the some check on both of its children as well if 
        # either of them return false then the binary tree is not a heap.
        return self.isHeapOrder(leftChild) or self.isHeapOrder(rightChild)
    
    # This function checks if the binary tree is complete or not
    def isBTComplete(self,root):
        if not root:
            return True
        # For that we will do a level order traversel over the binary tree
        # using a queue from left to right direction and the first null that
        # we find should be the find last node there shouldnt come any nodes
        # after because if it does then that means all the nodes are not to
        # the left of the tree since we traversing from left to right therefore
        # if this happens it means the tree is not complete and we can return False
        queue = Queue()
        isNull = False
        
        queue.put(root)
        
        while not queue.empty():
            node = queue.get()
            
            if node.left:
                # If after getting a null we find a node hence binary
                # tree is not complete and we return False
                if not isNull:
                    queue.put(node.left)
                else:
                    return False
            else:
                # If current node is null hence we shouldnt find any
                # nodes after this so we set isNull to True
                isNull = True
            
            if node.right:
                # If after getting a null we find a node hence binary
                # tree is not complete and we return False
                if not isNull:
                    queue.put(node.right)
                else:
                    return False
            else:
                # If current node is null hence we shouldnt find any
                # nodes after this so we set isNull to True
                isNull = True
        # If we exit loop without return a False hence binary tree is
        # complete
        return True
                    
    def isHeap(self, root):
        return self.isHeapOrder(root) and self.isBTComplete(root)
        