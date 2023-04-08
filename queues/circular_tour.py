def tour(lis, n):
        
        # Two pointers one which is going to denote the starting point
        # another pointer which is going to move as well travel from 
        # station to station
        front = 0
        rear = 0
        
        # Its going to store the balance petrol we have after travelling
        # from a station
        balance = 0
        
        # Running a while loop that runs until we have checked 
        # all stations and tries to find the first station that allows
        # us to make a circular tour around all the stations and 
        # without exhausting the petrol in between any of the stations.
        while front < n:
            
            balance+=(lis[rear][0] - lis[rear][1])
            
            # If difference is positive then that means we were able
            # to make it to the next station successfully
            
            if balance >= 0:
                
                rear = (rear + 1) % n

                if front == rear:
                    return front
                    
            # If difference is less than 0 then that means its not 
            # possible to make it to the next station from my current
            # station then i direcly move to that station i couldnt
            # get and check from there.
            else:
                front = rear+1
                rear = front
                balance = 0
        
        return -1
    
lis = [(6,5),(5,7),(4,4),(7,5),(4,5),(6,3)]

print(tour(lis,len(lis)))

def tour(lis, n):
        
        start = 0
        
        # This is going store the deficits that we get when we are not
        # able to get to a particular station.
        deficit = 0
        
        # The balance petrol that we have left after travelling from
        # a particular station.
        balance = 0
        
        # Then we make only one traversel for our rear
        for rear in range(n):
            
            # Adding my balance and my current stations petrol 
            # to see if we have enough to travel to our next
            # station.
            balance+=(lis[rear][0] - lis[rear][1])
            
            # If balance is less than zero then that means we didnt
            # have enough petrol to get to the next station hence
            # we have a deficit and we store it and see if we will
            # be able to cover it from the next starting point 
            if balance < 0:
                deficit+=balance
                start = rear+1
                balance = 0
        
        # If the balance from the starting point covers the deifict
        # that the previous stations had in order to get to the current
        # start then we can make a circular traversel through them.
        if (deficit + balance) >= 0:
            return start
        else:
            return -1
