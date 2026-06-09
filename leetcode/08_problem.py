def maxTotalSubarray(nums,k):
    mx = nums[0]
    mn = nums[0]
    
    for i in nums:
        if i > mx:
           mx = i
        if i < mn:
            mn = i
    print ((mx - mn)*k)    

m = maxTotalSubarray([1,5,2],3)    
                