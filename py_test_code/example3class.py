##this is an example of class in python3
##In this example we test class inheritance,class constructor,multiple classes and also class built in attributes
import time
class Acc_person:
    fname='';
    lname='';
    dob='';
    gen='';
    pwd='';
    mnumbr=00;
    def __init__(self):
        self.fname=input("Enter Your First Name:");
        self.lname=input("Enter Your Last Name:");
        self.dob=input("(dd-mm-yy)\nEnter Your Date Of Birth:");
        self.dob_year=int(self.dob[6:]);
        self.gen=input("Enter Your Gender:");
        self.pwd=input("Enter Your Password:");
        check=input("Enter Again:");
        while check!=self.pwd:
            check=input("Enter Again:");
        self.mnumbr=int(input("Enter Your Mobile Number:"));
    def person_age(self):
        self.current_time=int(time.strftime("%Y",time.localtime(time.time())));
        self.age_person=self.current_time-self.dob_year;
class up_Acc_person(Acc_person):
    #print("Upload Profile Picture");
	#pro_pic=str(input("Enter the Address Of Picture:"));
    def __init__(self):
        super(up_Acc_person,self).__init__();
        self.addrs=str(input("Enter Address:"));
        self.work=str(input("What do you do?"));
        self.status=str(input("Add your status here:"));
    def __vot(self):
        self.__acc_number=input("Enter your Account Number(don't worry it's safe):");
## Accesing these classes here
person=up_Acc_person();
person.person_age();
if person.age_person>=18:
    person._up_Acc_person__vot();
