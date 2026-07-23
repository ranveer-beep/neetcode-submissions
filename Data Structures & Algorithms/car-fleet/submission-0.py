class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(pos, spe) for pos, spe in zip(position, speed)]
        cars.sort(reverse = True)
        # hashmap 
        # sort by position (descending)
        # variables - arrival times
        # usa a stack to organise the fleets, pop the stack to find a car 
        #that arrives before the other car to organise the fleets
        # distance/speed = time 
        # same time => part of one fleet 
        # number of unique times is the number of fleets

        fleet = 1
        prevcartime= (target - cars[0][0])/ cars[0][1]
        for i in range(1, len(cars)):
            currcar = cars[i]
            currcartime = (target - currcar[0])/currcar[1]

            if currcartime > prevcartime:
                fleet +=1
                prevcartime = currcartime

        return fleet
            
