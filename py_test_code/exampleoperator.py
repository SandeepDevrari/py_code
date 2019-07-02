##this is an example of basic operator in python
#Arithmatic operators
i=2;
j=3;
p=i+j;
print(p);
p=i-j;
print(p);
p=i*j;
print(p);
p=i/j;
print(p);
p=i%j;
print(p);
p=i**j;
print(p);
p=i//j;
print(p);
##comparisoin operators
print("is i==j:"+str(i==j));
print("is i!=j:"+str(i!=j));
print("is i>j:"+str(i>j));
print("is i<j:"+str(i<j));
print("is i>=j:"+str(i>=j));
print("is i<=j:"+str(i<=j));
##Assignment operators
p=j;
print(str(p));
p-=i;
print(str(p));
p+=i;
print(str(p));
p*=i;
print(str(p));
p/=i;
print(str(p));
p%=i;
print(str(p));
p%=i;
print(str(p));
p**=i;
print(str(p));
p//=i;
print(str(p));
##Bitwise operators
#a=bin(i);
#b=bin(j);
#print(a,b);
p=i&j;
print("a:"+bin(i)+"\tb:"+bin(j)+"\ta&b:"+bin(p));
p=i|j;
print("a:"+bin(i)+"\tb:"+bin(j)+"\ta|b:"+bin(p));
p=i^j;
print("a:"+bin(i)+"\tb:"+bin(j)+"\ta^b:"+bin(p));
p=~i;
print("a:"+bin(i)+"\t~a:"+bin(p));
p=i>>j;
print("a:"+bin(i)+"\tb:"+bin(j)+"\ta>>b:"+bin(p));
p=i<<j;
print("a:"+bin(i)+"\tb:"+bin(j)+"\ta<<b:"+bin(p));
##Logical operators
a=True;
b=False;
print(a and b);
print(a or b);
print(not(a and b));
##Membership operators
print(i in [1,2,3,4,5,6]);
print(j in [1,2,4,5,6,7]);
##Identity operators
print("identity of i:"+str(id(i))+"\tidentity of j:"+str(id(j)));
print(i is j);
print(i is not j);