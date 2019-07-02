##this is an example of class
class product:
    pname=""
    pprice=00
    pqty=0
    ptype=""
    def data(self,pname,pprice,pqty,ptype):
        self.pname=pname
        self.pprice=pprice
        self.pqty=pqty
        self.ptype=ptype
    def show(self,q):
        print("name:"+self.pname)
        print("price:"+str(self.pprice))
        print("quantity:"+str(self.pqty))
        print("type:"+self.ptype)
        print("total amount:"+str(q))
    
    def cal(self):
        q=self.pprice*self.pqty
        return q
    def inputd(self):
        a=str(input("enter product name:"))
        b=int(input("enter product price:"))
        c=int(input("enter product quantity:"))
        d=str(input("enter product type:"))
        return a,b,c,d
try:
    p=product()
    pname,pprice,pqty,ptype=p.inputd()
    p.data(pname,pprice,pqty,ptype)
    q=p.cal();
    p.show(q);
except ValueError as V:
    print(V);