# missing number using xor


def missingNumber(nums): 
    result = len(nums)
    for i in range(len(nums)):
        result^=i^nums[i]
    
    return result    
    

nums =[9,8,6,4,3,2,1,0,5]
print(missingNumber(nums))

#  using dictionary 

# def missingNumber(nums): 
#     freq = {}
#     for i in range(0, len(nums)+1):git 
#         freq[i] = 0

#     for i in range(0, len(nums)):
#         freq[nums[i]] = 1

#     for k,v in freq.items():
#         if v == 0:
#             return k      
    

# nums =[9,8,6,4,3,2,1,0,5]
# print(missingNumber(nums))

       