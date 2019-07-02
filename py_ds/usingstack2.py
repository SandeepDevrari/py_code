##this is an example of stack
##in this progame we implement a base converter with the help of stack
import examplemenu;
import sys;
class converter(examplemenu.menu):
    def __init__(self):
        self.base_dict={'1':'decimal','2':'binary','3':'octal','4':'hexadecimal'};
        super(converter,self).__init__("decimal","binary","octal","hexadecimal");
        self.base_frm=examplemenu.menu.menu_return(self);
        ##print(self.base_frm);
        if self.base_frm not in self.base_dict:
            print("you entered wrong choice!!");
            exit(0);
        self.data=input("enter %s string:"%(self.base_dict[self.base_frm]));
        self.base_dict={'1':10,'2':2,'3':8,'4':16};##modified data
        self.digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'A':10,'b':11,'B':11,'c':12,'C':12,'d':13,'D':13,'e':14,'E':14,'f':15,'F':15};
        self.choose();

    def to_decimal(self,data,base_frm):
        base_digit=self.base_dict[base_frm];
        value=0;
        powr=0;
        data=list(data);
        for i in data[::-1]:
            if i in self.digits:
                i=self.digits[i];
            value+=i*base_digit**powr;
            powr+=1;
        for i, e in self.digits.items():
            if e==value:
                value=i;
                break;
        return value;

    def frm_decimal(self,div,base_to):
        import examplestack;
        base_digit=self.base_dict[base_to];
        div=int(div);
        stk=examplestack.stack();
        while div!=0:
            rem=div%base_digit;
            stk.push(rem);
            div=div//base_digit;
        value="";
        while not stk.is_empty():
            value=value+str(stk.pop());
        return value;

    def to_binary(self,data,base_to):
        data=list(data);
        value1="";
        for i in data:
            i=self.digits[i];
            value1=value1+self.frm_decimal(i,base_to);
        return value1;

    def frm_binary(self,data1,base_to):
        data1=list(data1);
        base_digit1=self.digits[base_to];
        value2=[];
        import examplestack;
        stk=examplestack.stack();
        while True:
            rem=len(data1)%base_digit1;
            if rem==0:
                count=0;
                for i in data1[::-1]:
                    count+=1;
                    if count==base_digit1:
                        stk.push(i);
                        count=0;
                        string="";
                        while not stk.is_empty():
                            string=string+stk.pop();
                        value2.append(self.to_decimal(string,'2'));
                    else:
                        stk.push(i);
                value1="";
                for i in value2[::-1]:
                    value1=value1+i;
                return value1;
            else:
                for q in range(1,(base_digit1-rem)+1):
                    data1.insert(0,'0');

    def b_to_b(self,data,base_to):
        value4=self.to_binary(data,'2');
        final_value=self.frm_binary(value4,base_to);
        return final_value;

##main function start from here
    def choose(self):
        if self.base_frm=='1':
            super(converter,self).__init__("binary","octal","hexadecimal");
            self.base_to=str(int(examplemenu.menu.menu_return(self))+1);
            if self.base_to=='2' or self.base_to=='3' or self.base_to=='4':
                self.value1=self.frm_decimal(self.data,self.base_to);
                print("your converted string is: %s"%(self.value1));
            #elif self.base_to=='2':
                #frm_decimal();
            else:
                #frm_decimal();
                print("you entered wrong!!");
        elif self.base_frm=='2':
            super(converter,self).__init__("decimal","octal","hexadecimal");
            self.base_to=examplemenu.menu.menu_return(self);
            if self.base_to=='1':
                self.value1=self.to_decimal(self.data,self.base_frm);
                print("your converted string is: %s"%(self.value1));
            elif self.base_to=='2' or self.base_to=='3':
                self.base_to+=1;
                self.value3=self.frm_binary(self.data,self.base_to);
                print("your converted string is: %s"%(self.value3));
            else:
                #to_hexa();
                print("you entered wrong!!");
        elif self.base_frm=='3':
            super(converter,self).__init__("decimal","binary","hexadecimal");
            self.base_to=examplemenu.menu.menu_return(self);
            if self.base_to=='1':
                self.value1=self.to_decimal(self.data,self.base_frm);
                print("your converted string is: %s"%(self.value1));
            elif self.base_to=='2':
                self.value1=self.to_binary(self.data,self.base_to);
                print("your converted string is: %s"%(self.value1));
            elif self.base_to=='3':
                self.base_to=str(int(self.base_to)+1);
                self.value1=self.b_to_b(self.data,self.base_to);
                print("your converted string is: %s"%(self.value1));
            else:
                print("you entered wrong!!");
        else:
            super(converter,self).__init__("decimal","binary","octal");
            self.base_to=examplemenu.menu.menu_return(self);
            if self.base_to=='1':
                self.value1=self.to_decimal(self.data,self.base_frm);
                print("your converted string is: %s"%(self.value1));
            elif self.base_to=='2':
                self.value1=self.to_binary(self.data,self.base_to);
                print("your converted string is: %s"%(self.value1));
            else:
                self.value1=self.b_to_b(self.data,self.base_to);
                print("your converted string is: %s"%(self.value1));
convert=converter();
