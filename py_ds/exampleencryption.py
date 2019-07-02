##this is a program for encryption
#n=str(input("enter ur name:"))
pas=str(input("enter your password:"))
for i in pas:
    p=ord(i)	#convert into int
    #print(p)
    p=p+2
    o=chr(p)	#convert into chr
    print(str(o),end='')
print('')
print("this is th encrypted password")