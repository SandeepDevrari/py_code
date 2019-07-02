##this is an example of command line argument 
import sys
len1=len(sys.argv[0])
print(str(len1))
len2=len(sys.argv)
print(str(len2))
print(sys.argv[1:])
if len2>1:
    print("arguments:",sys.argv)
print("####")


    
