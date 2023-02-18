L1=[]
L1=[12,-7,5,64,-14]
for i in L1:
    if i<0:
        L1.remove(i)
        for k in L1:
            if k<0:
                L1.remove(k)
                print(L1)
L2=[]
L2=[12,14,-95,3]
for j in L2:
    if j<0:
        L2.remove(j)
        print(L2)
