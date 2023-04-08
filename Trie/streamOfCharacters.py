from string import ascii_letters
from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.flag = False
    
    def containsKey(self,char: str) -> bool:
        return self.links[ascii_letters.index(char)]
    
    def insertKey(self,char: str,trieNode):
        self.links[ascii_letters.index(char)] = trieNode
    
    def getRefNode(self,char: str):
        return self.links[ascii_letters.index(char)]

    def setEnd(self):
        self.flag = True
    
    def getFlag(self):
        return self.flag

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word: str) -> None:
        node = self.root

        for char in reversed(word):
            if not node.containsKey(char):
                node.insertKey(char,TrieNode())
            node = node.getRefNode(char)
        
        node.setEnd()

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = ""
        for word in words: self.trie.insert(word)

    def query(self, letter: str) -> bool:        

        self.stream+=letter
        node = self.trie.root

        for char in reversed(self.stream):
            if not node.containsKey(char):
                return False
            node = node.getRefNode(char)
            if node.flag:
                return True 
            