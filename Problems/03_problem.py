def avg():
    nums = [1,2,3,5,9,7,6,4]
    sum = 0
    for i in range(0,len(nums)):
        sum +=i
    avg = sum/len(nums)
    
    return ("Total Sum: ", sum, "Average: ", avg)
print(avg())


    
        