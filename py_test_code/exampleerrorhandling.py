##this is an example of error handling
try:
    n=int(input("enter any number:"))
    n=n*2
    print(n)
except NameError as n:
    print(n)
except ValueError as v:
    print(v)
finally:
    print("clean up!")
