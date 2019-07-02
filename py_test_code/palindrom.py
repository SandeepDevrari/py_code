def palindrom():
    str=input("Enter Any String: ")
    #j=0
    for i in str[::-1]:
        if i==str[j]:
            j+=1
        else:
            print("NOT palindrom!!")
palindrom()