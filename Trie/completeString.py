import string
from typing import List

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containKey(self,char: str) -> bool:
        return bool(self.links[string.ascii_letters.index(char)])

    def insertKey(self,char: str,trieNode: 'TrieNode') -> None:
        self.links[string.ascii_letters.index(char)] = trieNode

    def getRefNode(self,char: str) -> 'TrieNode':
        return self.links[string.ascii_letters.index(char)]

    def setEnd(self) -> None:
        self.flag = True    

    def getFlag(self) -> bool:
        return self.flag  

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word: str):

        node = self.root

        for i in range(len(word)):
            char = word[i]

            if not node.containKey(char):
                node.insertKey(char,TrieNode())

            node = node.getRefNode(char)
        
        node.setEnd()
    
    def search(self,word: str):

        node = self.root

        for i in range(len(word)):
            char = word[i]

            node = node.getRefNode(char)

            if not node.getFlag():
                return False

        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        longestStr = ""

        for word in words:
            trie.insert(word)

        for word in words:
            if trie.search(word):
                if len(longestStr) < len(word):
                    longestStr = word
                elif len(word) == len(longestStr) and word < longestStr:
                    longestStr = word

        return longestStr