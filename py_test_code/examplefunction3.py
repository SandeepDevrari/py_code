##this is an example of function
def tri():
    a=0
    s='$'
    for i in range(4):
        for e in range(a,i):
            print(s,end='');
        print('');
    b=int(input("enter b:"));
    h=int(input("enter h:"));
    area=0.5*b*h;
    print("area:"+str(area));
#tri();

def rec():
    #a=0
    #s='*'
    for i in range(4):
        for e in ['*','*','*','*','*']:
            print(e,end='');
        print('');
    l=int(input("enter l:"));
    w=int(input("enter w:"));
    area=l*w;
    print("area:"+str(area));
#rec();


def squ():
    for i in range(5):
        for e in ['#','#','#','#','#']:
            print(e,end='');
        print('');
    #b=int(input("enter b:"));
    s=int(input("enter s:"));
    area=s*s;
    print("area:"+str(area));
#squ();

print("t/T for triangle\nr/R for rectangle\ns/S for square");
ch=str(input("enter ur choice:"));
if ch=='t' or ch=='T':
    tri();
elif ch=='r' or ch=='R':
    rec();
elif ch=='s' or ch=='S':
    squ();
else:
    print("u enter wrong!!!###");
