nums3 = [1,2,2,3,2,4]
d = {}
for i in range(0,11):
    d[i]= 0
    
   
for i in range(len(nums3)):
        d[nums3[i]] += 1    
    

for k,v in d.items():
    if(v>=1):
        print(k)            

        