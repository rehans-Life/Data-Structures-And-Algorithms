def createSequence(n):
  ans=[]
  def helper(n,sequenceNumber=0):
    
    if sequenceNumber >= n:
        return
    if sequenceNumber != 0:
        ans.append(sequenceNumber)
    
    sequenceOfTwo= ((sequenceNumber * 10 ) + 2)
    sequenceOfFive = ((sequenceNumber * 10 ) + 5)

    helper(n,sequenceOfTwo)
    helper(n,sequenceOfFive)
    
  helper(n)
  return ans 
print(createSequence(60))