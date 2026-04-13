nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum = 0
maxSum = nums[0]
for i in range(0, len(nums)):
    sum = sum+nums[i]
    if(sum> maxSum):
        maxSum = sum
    if(sum<0):
        sum = 0
print(maxSum)       
            