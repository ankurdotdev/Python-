# missing number using xor


def missingNumber(nums): 
    result = len(nums)
    for i in range(len(nums)):
        result^=i
        result^=nums[i]
    
    return result    
    

nums =[9,8,6,4,3,2,1,0,5]
print(missingNumber(nums))
        