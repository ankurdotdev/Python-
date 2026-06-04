arr = [11,2,3,5,6,8,9,11]
l1 = float('-inf')
l2 = float('-inf')

for i in range (len(arr)):
    if arr[i] > l1:
        l2 = l1
        l1 = arr[i]
    
    elif arr[i] > l2 and arr[i] != l1:
        l2 = arr[i]
        
print("Second largest >", l2)        
        
         
        