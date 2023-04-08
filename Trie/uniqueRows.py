
class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 2
        self.flag = False
    
    def containsKey(self,num):
        return self.links[num]
    
    def insertKey(self,num,trieNode):
        self.links[num] = trieNode
    
    def getRefNode(self,num):
        return self.links[num]
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def isUnique(self,row) -> bool:
        
        node = self.root
        
        for num in row:
            
            if not node.containsKey(num):
                node.insertKey(num,TrieNode())
            
            node = node.getRefNode(num)
        
        res = False if node.flag else True
        node.flag  = True
        
        return res 
        
def uniqueRow(matrix):
    trie = Trie()
    res = []
    
    for row in matrix:
        if trie.isUnique(row):
            res.append(row)
    
    return res

matrix = [[1,1,0,1],[1,0,0,1],[1,1,0,1]]
print(uniqueRow(matrix))