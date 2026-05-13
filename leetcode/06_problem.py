nums = [1,2,0,4,3,0,5,0,3,5,1,0]

# approach one

# i = 0
# while i < len(nums):
#     if nums[i] == 0:
#         break
#     i=i+1
# j = i+1   
# while j < len(nums):
#         if nums[j]!=0:
#             nums[i],nums[j] = nums[j],nums[i]  
#             i = i+1
#         j=j+1     
# print(nums)       

# approach second

# t1 = []
# t2 = []
# for i in range (len(nums)):
#     if nums[i]==0:
#         t2.append(nums[i])
#     else:
#         t1.append(nums[i])
# nums.clear()
# nums.extend(t1+t2)     
# nums[:] = t1+t2       

# print(nums)

# approach second

j = 0
for i in range(len(nums)):
    if nums[i] !=0:
        nums[j],nums[i] = nums[i],nums[j]
        j = j+1
print(nums)        