# find max and min element
def ele():
    nums = [1,2,3,5,8,9,7,6,4,11]
    max = nums[0]
    min = nums[0]
    
    for i in nums:
        if( i> max):
            max = i
        if(i<min):
            min = i     
    return max, min
print(ele())       
            