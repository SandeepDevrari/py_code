##this is an example of if else & elif
w=input("enter 'p' for picnic and 'e' for educational toure: ");
if w=='p' or w=="P":
    ch=int(input("enter charges:"));
    if ch>5000:
        print("EXPENSIVE");
    else:
        print("NOMINAL");
elif w=="e" or w=="E":
    r=input("'i' for industrial and 'e' for enterprinol: ");
    if r=='i' or r=='I':
        print("BORING!!!");
    elif r=='e' or r=='E':
        print("***EXCITING****");
    else:
        print("invalid character");
else:
    print("invalid character");