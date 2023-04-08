from typing import List
class Solution:
    def nearestSmallestToRight(self,histogram,stack,ouput):

        n = len(histogram)

        for i in reversed(range(n)):
            
            if len(stack) == 0:
                ouput[i] = n
                
            elif histogram[stack[len(stack)-1]] < histogram[i]:
                ouput[i] = stack[len(stack)-1]
                
            else:
                
                while len(stack) > 0 and histogram[stack[len(stack)-1]] >= histogram[i]:
                    stack.pop()
                
                if len(stack) == 0:
                    ouput[i] = n
                else:
                    ouput[i] = stack[len(stack)-1]                
            
            stack.append(i)

    def nearestSmallestToLeft(self,histogram,stack,ouput):
    
        n = len(histogram)
        
        for i in range(n):
            
            if len(stack) > 0:
                if histogram[stack[len(stack)-1]] < histogram[i]:
                    ouput[i]-=(stack[len(stack)-1]+1)
                else:
                    
                    while len(stack) > 0 and histogram[stack[len(stack)-1]] >= histogram[i]:
                        stack.pop()
                    
                    if len(stack) != 0:
                        ouput[i]-=(stack[len(stack)-1]+1)
                
            stack.append(i)

    def largestAreaHistogram(self,histogram):
        histogram = list(map(int,histogram))
        print(histogram)
        n = len(histogram)    
        stack = list()
        output = [0] * n
        
        self.nearestSmallestToRight(histogram,stack,output)
        stack.clear()
        self.nearestSmallestToLeft(histogram,stack,output)
        
        for i in range(n):
            output[i]*=histogram[i]
            
        return max(output)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        matrix = list(map(lambda x: list(map(int,x)),matrix))
        
        largestArea = 0
        
        for i,row in enumerate(matrix):
            
            if i - 1 < 0:
                largestArea = max(largestArea,self.largestAreaHistogram(row))
            else:
                
                for j in range(len(row)):
                    if row[j] != 0:
                        row[j]+=matrix[i-1][j]
                    
                largestArea = max(largestArea,self.largestAreaHistogram(row))
        
        return largestArea

matrix= [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
solution = Solution()
print(solution.maximalRectangle(matrix))