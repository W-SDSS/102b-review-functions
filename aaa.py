def midpoint(c1, c2):
    x=(c1(0)+c2(0))/2
    y=(c1(1)+c2(1))/2
    z=(c1(2)+c2(2))/2
    return x,y,z

print(midpoint([3,4,5],[10,20,30])) 

(6.5,12.0,17.5)