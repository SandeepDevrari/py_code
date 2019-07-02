##this is an example while loop
q=0
while q<=10:
    print(q);
    q=q+1


##this is for sum of no
q=1
t=0
n=int(input("enter loop no: "));
while q<=n:
    s=int(input("enter number: "));
    t=t+s
    q=q+1
print("total number"+str(q-1)+"of sum:"+str(t));

##another
c='y'
while c=='y' or c=='Y':
    w=input("enter ur name: ");
    print("length is"+str(len(w)));
    c=input("enter 'y' for again");
q=0;
##another again
while input("press SPACE to exit:").isalnum():
    q=q+1;
	#print(q);
else:
    print("you are exit!!");