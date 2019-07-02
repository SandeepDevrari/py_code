##this is an example of file handling
##simple file
f=open("file.txt",'w');
f.write("hello\n");
f.close()
##advance
f1=open("file.txt",'a');
s=str(input("enter name:"))
s1=str(input("enter password:"))
s2=str(input("enter DOB:"))
f1.write(s+"#"+s1+"#"+s2+"\n");
f1.close()
f2=open("file.txt",'r');
p=f2.read()
print(p)
f2.close();
