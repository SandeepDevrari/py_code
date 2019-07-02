#this is the actual implementation of examplestack.py
#here we import our examplestack file
#this program show the implementation of stack in python3
import examplestack
import sys
ch='2';	##for condition false
while ch!='1':
    ch=input("\t\t\tMENU-->\n\t\t1:create stack\n\tenter your choice:");
    if ch=='1':
        new_stack=examplestack.stack();
        print("stack is created##");
    else:
        print("enter valid choice!!");
while True:
    ch=input("\t\t\t\tMENU-->\n\t\t2:push stack\
       \n\t\t3:pop stack\n\t\t4:peek stack\n\t\t5:check stack empty\
       \n\t\t6:show stack\n\t\t7:exit\n\tenter your choice:");
    #if ch=='1':
        #new_stack=examplestack.stack();
        #print("stack is created");
    if ch=='2':
        data=input("enter data:");
        new_stack.push(data);
    elif ch=='3':
        print(new_stack.pop());
    elif ch=='4':
        print("top of stack is: "+new_stack.peek());
    elif ch=='5':
        print(new_stack.is_empty());
    elif ch=='6':
        print(new_stack.show_stack());
    elif ch=='7':
        print("you'r exit!!");
        exit(0);
    else:
        print("invalid choice!!!!");


