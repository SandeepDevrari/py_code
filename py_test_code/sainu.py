##this is an example
name=str(input("enter ur name:"))
name=name.lower();
k=0
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        k=k+1
print("no. of vowels in "+name+" is: "+str(k));
