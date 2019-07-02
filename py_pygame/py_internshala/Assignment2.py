##this is simple calculator script which can ADD,SUBTRACT,MULTIPLY and DIVIDE Complex Numbers
##author- Sandeep Devrari
##date-10/06/2017
##Assignment-2
def Add(x,y):
    print(x+y)

def Sub(x,y):
    print(x-y)

def Multi(x,y):
    print(x*y)

def Div(x,y):
    print(x/y)


def Module(x,y):
    print(abs(x))
    print(abs(y))

##main
check='Y'
while check=='Y' or check=='y':
    choice=input("\t\t\t\tMENU\n\t\t\t1-ADD\
                              \n\t\t\t2-SUBTRACT\
                              \n\t\t\t3-MULTIPLY\
                              \n\t\t\t4-DIVIDE\
                              \n\t\t\t5-MODULUS\
                              \n\t\tEnter: ")
    if choice>'0' and choice<'6':
        num1=complex(input("Enter Complex Number: "))
        num2=complex(input("Enter Second Complex Number: "))
        if choice=='1':
            Add(num1,num2)
        elif choice=='2':
            Sub(num1,num2)
        elif choice=='3':
            Multi(num1,num2)
        elif choice=='5':
            Module(num1,num2)
        elif num2!=0:
            Div(num1,num2)
        else:
            print("Error!!")
    else:
        print("Incorrect Choice!!")
    check=input("Want to Countinue(Y/N):")
else:
    print("EXIT!!")
