# Brute Force

# Space Complexity: O(n)
# Time Complexity: O(n^2)

import math
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:

        length_s = len(s) 
        answers = [0] * length_s
        
        for i in range(length_s):
            
            distance_from_c = math.inf

            for j in range(length_s):
                if s[j] == c:
                    distance_from_c = min(distance_from_c,abs(i-j))

            answers[i] = distance_from_c
        
        return answers

# Optimal - Linear Time

# Space Complexity - O(n)
# Time Complexity - O(n)

import math
def shortestToChar(s: str, c: str) -> list[int]:

        answer = [math.inf] * len(s)
        left = None
        right = None

        for i in range(len(s)):
            if s[i] == c:
                left = i

            if left is not None:
                answer[i] = abs(i - left)
                
        for j in reversed(range(len(s))):
            if s[j] == c:
                right = j
            
            if right:
                answer[j] = min(answer[j],abs(j - right))
        
        return answer

# print(shortestToChar('baaa','b'))