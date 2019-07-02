class Rectangle:
    length=0;
    width=0;
    def print_area(self):
        print("area: ",self.length*self.width);

obj1=Rectangle();
obj1.length=4;
obj1.width=5;
obj1.print_area();
obj2=Rectangle();
obj2.length=6;
obj2.width=7;
obj1.print_area();