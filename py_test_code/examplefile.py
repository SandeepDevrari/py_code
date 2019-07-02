##this is an example of file handling in python
import os
i=str(input("enter a file name:"));
f1=open(i,'w');
f1.write("this is an example of file handling in python3");
f1.close();
f2=open(i,'r');
print("simple read:"+f2.read());
f2.close();
f2=open(i,'a');
f2.write("\nhello again");
f2.close();
f2=open(i,'a+');
print("read in appending mode:%s"%f2.read(15));
f2.close();
f2=open(i,'r');
print("read a single line:"+f2.readline());
print("current position:"+str(f2.tell()));
pos=f2.seek(0,0);
s=f2.readlines();
print("read multiple lines:%s"%(s));
#print("mode:"+str(f2.mode()));
#print("file name:"+f2.name());
f2.close();
#os.rename(i,"ye.txt");