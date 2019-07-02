##this is an example of exception handling
try:
    i=int(input("enter any value:"));
    i=i/0;
    #print(str(i));
except ZeroDivisionError as v:
    print(v);
finally:
    print("son:kani\npapa:sainu");