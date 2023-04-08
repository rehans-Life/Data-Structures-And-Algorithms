def generateIPAddress(s):
    # Write your code here.
    ans = []
    
    def helper(i=0,ipAddress=[]):
        
        # When i have used up all of the given elements then i obviously need to stop.
        
        # But if i have used up all of the given elements and generated an IP address with length
        # of 4 then i append that IP Address to my answer since its a valid IP Address.
        
        # But if i have used up all of the given elements and still didnt generate an IP Address of 
        # length of 4 then I Stop without adding the IP Address to my answer since the IP Address
        # is invalid.
        
        if i == len(s):
            if len(ipAddress) == 4:
                ans.append('.'.join(ipAddress.copy()))
            return
        
        # If i have not used up all the integers in the string and still generated a IP Address of length
        # of 4 then i need to stop cause i have generated an invalid IP Address.
        
        if len(ipAddress) == 4:
            return
        
        # Recursive Calls.
        
        # Using only the Ith element
        
        # Appending on the Ith Element to the answer
        ipAddress.append(s[i])
        
        # Making recursive call to fill out rest of the integers in the IP Address
        helper(i+1,ipAddress)
        
        # After i have finished with the recursive function either cause i maybe generated IP Address or
        # I generated a invalid IP Address either way I need to backtrack and undo the changes that I made
        # while generating a partcular IP Address so that other IP Addresses can also be generated.
        ipAddress.pop()
        
        # So if a integer actually exists next to ith integer then i consider the case of taking the pair
        # integers
        if s[i] != '0':
            if i + 1 < len(s):
                # Appending the ith integer and the integer next to it to my IP Address
                ipAddress.append(s[i:i+2])

                # Making recursive call to fill out rest of the integers in the IP Address
                helper(i+2,ipAddress)

                # Backtracking the poping the pair out cause im going to make another recursive with pair of three
                ipAddress.pop()
            
            # So if there is a third integer next to the ith integer then i consider the case of taking the pair
            # of three.
            if i + 2 < len(s)  and int(s[i:i+3]) <= 255:
                # Appending the ith itenger and the two integers next to it to my IP Address
                ipAddress.append(s[i:i+3])

                # Then making a recursive call to fill our rest of the integers in the IP Address
                helper(i+3)

                # Then undoing the change that i made after the recursive function is done executing.
                ipAddress.pop()
    helper()
    return sorted(ans)
print(generateIPAddress('023456'))