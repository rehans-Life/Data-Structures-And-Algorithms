import string

class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.flag = False

    def containsKey(self,char: str) -> bool:
        return  bool(self.links[string.ascii_letters.index(char)])

    def insertKey(self,char: str,trieNode: 'TrieNode') -> None:
        self.links[string.ascii_letters.index(char)] = trieNode
    
    def getRef(self,char: str) -> 'TrieNode':
        return self.links[string.ascii_letters.index(char)]
    
    def setEnd(self) -> None:
        self.flag = True
    
    def getFlag(self) -> bool:
        return self.flag
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            char = word[i]
            
            if not node.containsKey(char):
                node.insertKey(char,TrieNode())            
                
            node = node.getRef(char)
            
        node.setEnd() 
    
        
    def search(self,word: str) -> bool:
        node = self.root
        
        for i in range(len(word)):
            char = word[i]
            
            if not node.containsKey(char):
                return False

            node = node.getRef(char)
            
        return node.getFlag()
        
    def startsWith(self,prefix: str) -> bool:
        node = self.root
        
        for i in range(len(prefix)):
            char = prefix[i]
            
            if not node.containsKey(char):
                return False
            
            node = node.getRef(char)
        
        return True
    
    
    