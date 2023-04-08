from queue import Queue
from string import ascii_lowercase
from typing import * 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # We are going to be using a combination of brute force approach to generate  all the sequences with a bfs
        # traversel to detect the endWord in our sequence and count the length of our shortest sequence.

        # A queue to store our sequences and perform bfs over them
        queue =  Queue()

        # We know all sequences will start from the beginWord so we intially add it to the queue along
        # with the length of the sequence with it which is initially one as well cause beginWord is the
        # first word in the sequence
        queue.put([beginWord,1])

        # Then also we need to make sure we dont add the same words back into the sequences that we generate

        # So we need to delete them from our wordList as we add them to our sequence so no other sequence can
        # have this word neither the same sequence can insert it back into itself.

        # And set allows us efficient deletion and searching so we gon convert our wordList into a set.
        wordList = set(wordList)

        while not queue.empty():

            # Take the top word out and destructure it out with the length of the sequence
            word,length = queue.get()
            n = len(word)

            # Then we need to generate all possible words that could exist after this word within the 
            # sequence so for that we replace each character with all 26 alphabets and check if the word
            # formed after the replacement exists within the wordlist if it does then it can exist after
            # this word within the sequence.

            # So we need to go through each character in the word and replace it will all 26 alphabets and check
            for i in range(n):
                # ascii_lowercase is from the library 'string' and its gives a string with all alphabets
                for alphabet in ascii_lowercase:
                    # Since strings are immutable in python im going to use string slicing to replace the
                    # character within the word
                    newWord = word[0:i] + alphabet + word[i+1:n]
                    # Then we check if the new word exists within our wordList or not if it does then we add 
                    # to our queue cause its going to come after this word in the sequence
                    if newWord in wordList:

                        # We also check if the newWord is our target word or not if it is then return the length
                        # of thr sequence with this word
                        if newWord == endWord:
                            return length+1

                        # We also remove the word from the wordList so it cant get inserted again
                        wordList.remove(newWord)
                        # With the new word of the sequence the length incrments by one
                        queue.put([newWord,length+1])

        # If we exit the loop then that means the startWord couldnt be converted into the target word        
        return 0




