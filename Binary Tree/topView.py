from queue import Queue

class Solution:
    def topView(self,root):
        
        # A queue to make our level order traversel from top to bottom
        # of the subtree
        queue = Queue()
        
        # A hashmap to map all columns to there top most node values
        cols = dict()
        
        # Initally we insert the root node with its column in the queue
        queue.put([root,0])
        
        while not queue.empty():
            
            # Extracting the top most node out of the queue
            node = queue.get()
            col = node[1]
            # Inserting the nodes left child and right child back into 
            # the queue with there respective columns.
            if node[0].left:
                queue.put([node[0].left,col-1])
                
            if node[0].right:
                queue.put([node[0].right,col+1])
            
            # Then i will check if the current nodes column is not mapped
            # to any nodes cause if it isnt then this node is the top
            # most node of its column so i can set it to that column
            # number since its going to be view from the top
            
            # But its already mapped then this guy is under some 
            # node and wont be seen 
            
            # Only the top most nodes will be seen
            if col not in cols:
                cols[col] = node[0].data
        
        
        return [val for key,val in sorted(cols.items())]