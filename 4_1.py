x1 = [3, 10, 5, 25, 2, 8]
def xor():
    c=0
    for i in range(0,len(x1)-1):
        for j in range(i+1,len(x1)):
                    c1=(x1[i]^x1[j])
                    if (c<c1):
                        c=c1
    print(c)                

xor()