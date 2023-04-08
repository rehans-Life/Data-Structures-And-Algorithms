# Optimal Approach

# Space Complexity: O(n)
# Time Complexity: O(n)

def getPairsCount(arr, n, k):
    
    # A Hashmap to store the counter each element in the array
    counter = dict()

    # Whenever i find a valid im going to increment this var
    ans = 0

    # Running an iteration for each number in the array and adding
    # that number to the hashmap and also checking if the number 
    # that this number forms a pair with to give us sum of k exists
    # in the array or not.

    # You can easily check the number that our current number needs
    # to form a pair with to get sum k by subtrating that number
    # from k. So (k-number) will give you that sum.

    for num in arr:

        # Computing the number the current number that this number
        # needs to form a pair with to get sum k
        val = k - num

        # Checking if that number is in the hashmap or not
        # if it is then we incrment our answer by the times that 
        # number exist in the array cause thats how many pairs
        # will be formed
        if val in counter:
            ans+=counter[val]
        
        # Adding/incrementing this number in the hashmap

        # If its not there we add it if its already there we
        # increment it by one.

        if num not in counter:
            counter[num] = 0
        
        counter[num]+=1

    return ans    


