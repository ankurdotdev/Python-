def max_three(a,b,c):
    if(a>b and a>c):
        print("a = ",a," is greater")
    elif(b>a and b>c):
        print("b = ",b," is greater")    
    elif(c>b and c>a):
        print("c = ",c, " is greater")
    else:
        print("all are equal")        
max_three(1,2,3)        
max_three(1,1,5)        
max_three(1,1,1)        