##this is simple calculator script which can ADD,SUBTRACT,MULTIPLY and DIVIDE
##author- Sandeep Devrari
##date-03/06/2017
##Assignment-1
def Add(x,y):
    print("Answer: ",x+y)

def Sub(x,y):
    print("Answer: ",x-y)

def Multi(x,y):
    print("Answer: ",x*y)

def Div(x,y):
    print("Answer: ",x/y)

##main
check='Y'
while check=='Y' or check=='y':
    choice=input("\t\t\t\tMENU\n\t\t\t1-ADD\
                              \n\t\t\t2-SUBTRACT\
                              \n\t\t\t3-MULTIPLY\
                              \n\t\t\t4-DIVIDE\
                              \n\t\tEnter: ")
    if choice>'0' and choice<'5':
        num1=float(input("Enter Number: "))
        num2=float(input("Enter Second Number: "))
        if choice=='1':
            Add(num1,num2)
        elif choice=='2':
            Sub(num1,num2)
        elif choice=='3':
            Multi(num1,num2)
        else:
            Div(num1,num2)
    else:
        print("Incorrect Choice!!")
    check=input("Want to Countinue(Y/N):")
else:
    print("EXIT!!")
