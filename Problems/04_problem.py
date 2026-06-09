#COUNT OF EVEN AND ODD NUMBERS IN AN ARRAY
def evenOdd():
   
    nums = [1,2,3,5,8,9,7,6,4,11]
    oddcount = 0
    evencount = 0
   
    for i in range(0,len(nums)):
       
        if(nums[i]% 2 == 0):
            evencount+=1
        else:
            oddcount+=1
    
    return ("Even Count: ", evencount, "Odd Count: ", oddcount)        

print(evenOdd())           
        
    


    
        