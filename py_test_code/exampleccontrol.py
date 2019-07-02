##this is an example of control statement
chal=input("press 2:");
#kal=int(chal);
if chal=='2':
    print("your Fool!!");
   # print(chal);
else:
    if chal.isalpha()==True:
        chal=str(input("enter your name:"));
        if chal.isdigit():
           # pass
            print("*****");

    pass
    for i in range(1,11):
        if i==9:
            continue
        print("#",end=' ');
