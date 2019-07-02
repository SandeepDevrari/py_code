##this is an example of tuples
tup=(8,4,5,"hello");
tup1=(1,);  #single value tuple
tup2=tup+tup1   #modifiying tup
print(tup);
f=1
#factorial of tuple value
for i in tup[0:3]:
    print("factorial of "+str(i));
    for e in range(1,i+1):
        f=f*e
    print(f);
    f=1
