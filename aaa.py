def gcflcm(n1,n2):
    number=max(n1,n2)
    answer=[]
    for i in range(1, number+1):
        if n1%i==0 and n2%i==0:
           answer.append(i)
           gcf=answer[-1]
    n1=[]
    n2=[]
    for i in range(1,number+1):
        
    return gcf,lcm


print(gcflcm(24,16))

8,48