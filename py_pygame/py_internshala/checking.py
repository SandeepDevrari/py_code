k=0;
for i in  range(1,6):
    for j in range(1,i):
        k+=1;
        if k%2!=0:
            print(k,end='')
        else:
            print("0",end='')
    print("")