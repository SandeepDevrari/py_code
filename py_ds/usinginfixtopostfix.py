#this is the program for converting infix to prefix using exampleinfixtopostfix
import exampleinfixtopostfix
class convert:
    def __init__(self):
        self.infix_data=input("enter infix expression: ");
        ##print("init value of data list: %s"%(self.infix_data));
        self.result=self.convertor(self.infix_data);
        h="";
        for i in self.result:
            h=h+i;
        print("postfix: %s"%(h));
    def convertor(self,data):
        self.check_pre=['0','1','2','3','4','5','6','7','8','9','(',')','^','*','/','%','+','-'];
        for i in data:
            if i not in self.check_pre:
                print("Error");
                exit(0);
        chk=['0','1','2','3','4','5','6','7','8','9'];
        chk1=['^','*','/','%','+','-'];
        v='';
        for i in data:
            if i in chk:
                v=v+i;
            else:
                i=' '+i+' ';
                v=v+i;
        ##print("init value of data string: %s"%(v));
        data=v.split();
        ##print("initialy value of data list: %s"%(data));
        obj=exampleinfixtopostfix.in_to_post(data);
        data=obj.return_bck();
        return data;
convertorr=convert();
