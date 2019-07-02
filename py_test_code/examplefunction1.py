##this is an example of variable length arguments
def fun(a,*s):
    print(str(s));
    print(str(a));
    for i in s:
        print(str(i));
fun(5,'w',9,7,'sainu');
fun('Hello');
