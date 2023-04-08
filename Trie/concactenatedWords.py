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

        for char in word:
            if not node.containsKey(char):
                node.insertKey(char,TrieNode())
            node = node.getRefNode(char)
        
        node.setEnd()
    
    def isConcactenatedWord(self,word: str,j : int,count: int) -> bool:

        # When we have reached the end of the word and if the concactenated word count is not
        # greater than one hence i can return a false else if it is then return True
        if j == len(word):
            return count != 1
        
        # A node pointer we keep moving the verify the characters
        node = self.root

        # Iterating through word 
        for i in range(j,len(word)):

            char = word[i]

            # If the word that we are checking that if it is a smaller word that is forming
            # our concactenated word if one of its characters does not make it match with the words
            # with in the array we return False
            if not node.containsKey(char): return False

            # Or else if character is matching we move to its reference node and check the next
            # character
            node = node.getRefNode(char)

            # If we find a word here hence therefore we need to check if the next part also forms a word
            # which exists inside of the array because this word to be a concactenated word it should entirely
            # be comprised of smaller words from the array but in this recursive call we increment count for 
            # this word that we have found.
            if node.getFlag():
                # If that part is also a smaller word then we get True and hence we can return  True
                if self.isConcactenatedWord(word,i+1,count+1):
                    return True

        # If we exit the loop hence we can return False then cause we werent able to find atleast two 
        # concactenated words
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        output = []
        trie = Trie()

        for word in words: trie.insert(word)

        for word in words:
            if trie.isConcactenatedWord(word,0,0):
                output.append(word)

        return output
        