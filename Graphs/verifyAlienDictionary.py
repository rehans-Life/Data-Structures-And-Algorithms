# Time Complexity: O(26 + (n * m)) => O(n * m)
# Space Complexity: O(1)

from typing import *
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)

        # Mapping each character of the english lowercase alphabets to its position in the alien
        # alphabetical order 
        position = {alphabet : i for i,alphabet in enumerate(order)}

        # Then comparing each pair of words within the sequences and checking if they are sorted or not
        for i in range(n-1):
            # Taking each consecutive pair and comparing them and seeing if they are in there sorted 
            # positions or not.
            word1 = words[i]
            word2 = words[i+1]
            w1 = len(word1)
            w2 = len(word2)
            # For that i need to find the first different characters b/w both the consective words
            # I only need to traverse the smaller words length for finding the first different character  
            smaller = w1 if w1 < w2 else w2

            for j in range(smaller):
                # Checking if the current corresponding characters are unequal and then we can compare
                if word1[j] != word2[j]:
                    # Since word1 exists before word2 in the sequence hence we know that its 
                    # differentiating character should come before the word2 character.
                    # If it doesnt then they are not sorted
                    if position[word1[j]] > position[word2[j]]:
                            return False
                    # If word1 differing character does exists before word2's character hence they
                    # are in there sorted positions hence we can move forward to next pair of words
                    # so we break out.
                    break            
            # If word2 is the prefix of the word1 hence they are not in there sorted positions so we can
            # return False
            if w2 < w1 and word2 in word1:
                return False

        return True