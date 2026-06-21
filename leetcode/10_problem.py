# Leetcode --> 1833. Maximum Ice Cream Bars
def maximumIcecream(costs, coins):
    costs.sort()
    count = 0
    
    for i in costs:
        if coins >= i:
            coins -= i
            count +=1
        else:
            break
        
    return count

m = maximumIcecream([1,3,2,4,1],7)        
print(m)