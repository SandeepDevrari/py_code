##this is an example of directory handlinng in python3
import os,sys
print("\t\t\tMENU");
while True:
    print("\t\t1:create directory\n\
    	    \t2:change directory\n\
    	    \t3:display current directory\n\
    		4:remove directory");
    ch=input("enter choice here:");
    if ch=='1':
        name=str(input("enter directory name:"));
        os.mkdir(name);
    elif ch=='2':
        chngdir=str(input("enter address here:"));
        os.chdir(chngdir);
    elif ch=='3':
        cwd=os.getcwd();
        print(cwd);
    elif ch=='4':
        rm=str(input("enter directory name:"));
        os.rmdir(rm);
    else:
        print("you are exit!!");
        exit();