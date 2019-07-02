#this is an another example of stack implementation
#this is the program for calculator
import examplestack
import sys
import exampleinfixtopostfix
class cal:
    def __init__(self):
        self.data=input("\n\t\t\tEnter: ");
        self.result=self.calci(self.data);
        print("\t\t\tResult: %s\n"%(self.result));
    def calci(self,data):
        self.check_pre=['0','1','2','3','4','5','6','7','8','9','(',')','^','*','/','%','+','-'];
        for i in data:
            if i not in self.check_pre:
                print("Error");
                exit(0);
        chk=['0','1','2','3','4','5','6','7','8','9'];
        chk1=['^','*','/','%','+','-'];
        v='';
        e=0;
        for i in data:
            if i in chk:
                v=v+i;
                e+=1;
            else:
                i=' '+i+' ';
                v=v+i;
        if e==0:
            print("Error");
            exit(0);
        self.data=v.split();
        stk=examplestack.stack();
        obj=exampleinfixtopostfix.in_to_post(self.data);
        self.data=obj.return_bck();
        for i in self.data:
            if i in chk1:
                oprend2=stk.pop();
                oprend1=stk.pop();
                result1=self.calculate(i,oprend1,oprend2);
                stk.push(result1);
            else:
                stk.push(int(i));
        return str(stk.pop());
    def calculate(self,operetor,oprend1,oprend2):
        if operetor=='+':
            return oprend1 + oprend2;
        elif operetor=='*':
            return oprend1 * oprend2;
        elif operetor=='/':
            return oprend1 / oprend2;
        elif operetor=='-':
            return oprend1 - oprend2;
        else:
            return oprend1 ** oprend2;
calculator=cal();
