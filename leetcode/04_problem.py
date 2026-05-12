def missingNumber(nums):
    actual_sum = 0
    exp_sum = 0
    l = len(nums)
    
    for i in range(l):
        actual_sum += nums[i]
        
    for i  in range(0,l+1):
        exp_sum = exp_sum + i    
        
    return exp_sum - actual_sum    
        

nums =[9,8,6,4,3,2,1,0,5]
print(missingNumber(nums))
