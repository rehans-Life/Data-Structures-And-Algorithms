from queue import Queue

class Solution:
    def bottomView(self, root):
        
        # A queue to store the child nodes i will be traversing through
        # so that in order to traverse the nodes of the next level i can
        # just take the nodes from queue itself.
        queue = Queue()
        
        # A hashmap to map the column number to that last node value
        # that we found representing that column in our tree while
        # traversing it from top to bottom.
        cols = dict()
        
        # Initially we add the root node in our queue along with its
        # column number which is zero for the root.
        queue.put([root,0])
        
        while not queue.empty():
            
            # Taking the top most node out of the queue
            node = queue.get()
            col = node[1]
            # Then we add its left child and right child along with there
            # column numbers.
            # back into the queue so we can traverse them later on by 
            # taking them out of the queue
            if node[0].left:
                queue.put([node[0].left,col-1])
            
            if node[0].right:
                queue.put([node[0].right,col+1])
                
            # I check if this column is already mapped to a value
            # or not if its not then we add it and set it to this
            # nodes value but if its already then i replace it 
            # cause since im traversing from top to bottom hence this
            # is the bottom most node that ive found this column
            # and i want the bottom most value for that column so i 
            # replace it with this nodes value
            if col not in cols:
                cols[col] = node[0].data
            else:
                cols[col] = node[0].data
            
        return [val for key,val in sorted(cols.items())]