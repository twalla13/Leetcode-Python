#https://leetcode.com/problems/car-fleet/description/

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    
    #Must pair (position, speed) and then sort then from closets to target to furthest from target
    #Zip => If position = [a, b, c] and speed = [x, y, z], zip produces an iterator over (a, x), (b, y), (c, z)
    cars = list(zip(position, speed))
    
    #sort reorders list in place
    #key=lambda x:x[0] tells python to look at first element in tuple
    #reverse= True reverse the order 
    
    cars.sort(key=lambda x: x[0], reverse=True)
    
    #create times array by using math
    #times should be in decreasing order
    times = [(target - pos)/ spd for pos, spd in cars]
    fleets = 0
    currentMax = 0
    
    #sweep and count
    for time in times:
        # If this car's arrival time is greater than any seen so far,
        # it cannot catch up to the fleet ahead and forms a new fleet
        if time > currentMax:
            currentMax = time
            fleets += 1
            
    return fleets