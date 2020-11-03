z = [1, 3, 4, 4, 2]
x=set(z)
def dubl():
    y=[]
    for i in x:
     if(z.count(i)>1):
          y.append(i)
    print(y)    

dubl()