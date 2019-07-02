##this is an example of tuples
tup1=(1,15,3,8,12);	#tuple
tup2=(2,3,8,6,9);
p=0
l=[]
o=0
l1=[]
q=0
w=0
for i in tup1:
    for e in tup2:
        if i==e:
            l.insert(o,p)
            o=o+1
    p=p+1
for e in tup2:
    for i in tup1:
        if e==i:
            l1.insert(w,q)
            w=w+1
    q=q+1
tup3=tup1[l[0]:l[1]+1]
tup4=tup1[:l[0]]+tup1[l[1]+1:]+tup2[:l1[0]]+tup2[l1[1]+1:]
print(tup3);
print(tup4);
#print(l)
#print(l1)
