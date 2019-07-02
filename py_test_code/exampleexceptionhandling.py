##this is an example exception handling
try:
    n=int(input("enter any number:"))
    print(n)
except NameError as n:
    print(n)
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)
finally:
    print("clean up####")
