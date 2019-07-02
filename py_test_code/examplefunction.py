##this is an example of fuction
#simple 
def fun():
    print("karan");
fun();

#advance

def per(n,gen):
    if gen=='m' or gen=='M':
        print("hello mr."+n);
    else:
        print("hello miss "+n);

def per1():
     n=str(input("enter ur name:"));
     gen=str(input("ur gender('m' for male and 'f' for female):"));
     return n,gen;
def per2():
    s,a=per1();
    per(s,a);
    i=input("enter ur mobile no:");
    print("u'r mobile no.:"+i);


#s,a=per1();
#per(s,a);
per2();
