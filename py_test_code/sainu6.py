n=str(input("enter ur name:"))
n=n.upper();
p=0
len1=len(n);
for i in range(len1+1):
   for c in range(p,i):
      print(n[c],end=' ');
   print("");
