##this is an another example
#class1
class pet:
    pname=""
    ptype=""
    pbreed=""
    page=0
    vac=""
    def indata1(self):
        a=str(input("enter pet name:"));
        b=str(input("enter pet type:"));
        c=str(input("enter pet breed:"));
        d=int(input("enter pet age:"));
        e=str(input("is pet vaccinated:"));
        return a,b,c,d,e;
    def data1(self,a,b,c,d,e):
        self.pname=a;
        self.ptype=b;
        self.pbreed=c;
        self.page=d;
        self.vac=e;
    def show1(self):
        print("name:"+self.pname);
        print("pet type:"+self.ptype);
        print("pet breed:"+self.pbreed);
        print("pet age:"+str(self.page));
        print("pet is :"+self.vac+" vaccinated");
#class2
class petshop:
    item="";
    price=00;
    def indata3(self):
        a=str(input("enter petshop item:"));
        b=int(input("enter item price:"));
        return a,b;
    def data3(self,a,b):
        self.item=a;
        self.price=b;
    def show3(self):
        print("item name:"+self.item);
        print("item price:"+str(self.price));
#inherited class
class owner(pet,petshop):
    name="";
    cont=00;
    email="";
    def indata2(self):
        a=str(input("enter owner name:"));
        b=int(input("enter owner contact:"));
        c=str(input("enter owner email:"));
        return a,b,c;
    def data2(self,a,b,c):
        self.name=a;
        self.cont=b;
        self.email=c;
    def show2(self):
        print("owner name:"+self.name);
        print("owner contact:"+str(self.cont));
        print("owner email:"+self.email);
##d=pet()
##z,x,c,v,b=d.indata1()
##d.data1(z,x,c,v,b)
##d.show1()
#owner
o=owner();
z,x,c=o.indata2();
o.data2(z,x,c);
o.show2();
#pet
z,x,c,v,b=o.indata1();
o.data1(z,x,c,v,b);
o.show1();
#petshop
z,x=o.indata3();
o.data3(z,x);
o.show3();