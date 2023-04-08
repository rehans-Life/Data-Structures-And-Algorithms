import string

class TrieNode:
    def __init__(self):
        self.links = [None] * 26

    def containsKey(self,char: str) -> bool:
        return self.links[string.ascii_letters.index(char)]

    def insertKey(self,char: str,trieNode):
        self.links[string.ascii_letters.index(char)] = trieNode

    def getRefNode(self,char: str):
        return self.links[string.ascii_letters.index(char)] 
    

def countDistinctSubstrings(s):

    root = TrieNode()
    ans = 1

    for i in range(len(s)):
        node = root
        for j in range(i,len(s)):
            char = s[j]
            if not node.containsKey(char):
                ans+=1
                node.insertKey(char,TrieNode())
            
            node = node.getRefNode(char)
    
    return ans