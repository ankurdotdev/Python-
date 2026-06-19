# leetcode -> 1732. Find the Highest Altitude
def largestAltitude(gain):
    curr = 0
    highest = 0
    
    for i in gain:
        curr += i
        
        if curr > highest:
            highest = curr
            
    return highest

gain = [-5,1,5,0,-7]
print(largestAltitude([-5,1,5,0,-7]))      
