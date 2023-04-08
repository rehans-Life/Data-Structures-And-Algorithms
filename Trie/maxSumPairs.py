from string import ascii_lowercase,ascii_letters

class TrieNode:
    
    def __init__(self) -> None:
        self.links = [None] * 26
        self.val = 0

    def containsKey(self,char: str) -> bool:
        return self.links[ascii_letters.index(char)]
    
    def insertKey(self,char: str,trieNode) -> None:
        self.links[ascii_letters.index(char)] = trieNode
    
    def getRefNode(self,char: str):
        return self.links[ascii_letters.index(char)]

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,key: str, val: int) -> None:
        node = self.root

        for char in key:

            if not node.containsKey(char):
                node.insertKey(char,TrieNode())
            
            node = node.getRefNode(char)
        
        node.val = val
    
    def sumKeys(self,prefix: str) -> int:

        sumation = 0
        node = self.root

        for char in prefix:

            if not node.containsKey(char):
                return 0
            
            node = node.getRefNode(char)
        
        # Now from our current node pointer we have to generate all words
        # that have this prefix find there values and sum them up
        def helper(curr):

            nonlocal sumation

            if curr.val != 0:
                sumation+=curr.val
            
            for char in ascii_lowercase:
                if curr.containsKey(char):
                    helper(curr.getRefNode(char))
        
        helper(node)

        return sumation

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root

        for char in key:

            if not node.containsKey(char):
                node.insertKey(char,TrieNode())
            
            node = node.getRefNode(char)
        
        node.val = val
    
    def checkPrefix(self,prefix: str):
        node = self.root

        for char in prefix:
            if not node.containsKey(char):
                return 0

            node = node.getRefNode(char)
        
        return node

    def sum(self, prefix: str) -> int:
        
        node = self.checkPrefix(prefix)
        sumation = 0

        # If there is no key with the prefix we return zero as sum
        if node == 0: return 0
        
        # Now from our current node pointer we have to generate all words
        # that have this prefix find there values and sum them up
        def helper(curr):
            nonlocal sumation
            
            # If there is a key at this current node then add its value to the given sum.
            if curr.val != 0:
                sumation+=curr.val
            
            # We find all possible words from the current by iterating throgh all characters from
            # a to z and checking which ones have reference noes cause the ones that do have reference
            # node there is a key with them.
            for char in ascii_lowercase:
                if curr.containsKey(char):
                    helper(curr.getRefNode(char))
        
        helper(node)
        
        return sumation
    
