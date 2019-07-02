##this is an example for testing functions in python3
def fun():
    name=input("enter anything:");
    age=int(input("enter any digit:"));
    return name,age;
fun1=lambda name,age:print("you entered:%s and %d" %(name,age));
##calling
name,age=fun();
fun1(name,age);
