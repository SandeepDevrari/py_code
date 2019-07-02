##this is an example of class
class student:
    def __init__(self):	#constructor
        self.a=int(input("enter ur roll number:"));
        self.b=str(input("enter ur name:"));
        self.c=str(input("enter ur course:"));
        self.d=int(input("enter ur sem:"));

    def data(self):	#funtion
        print("roll number:"+str(self.a)+"\nname:"+self.b+"\ncourse:"+self.c+"\nsem:"+str(self.d));

try:
    s=student();
    s.data();
    print(getattr(s,'b'));
    print(hasattr(s,'b'));
    setattr(s,'age',21);
except ValueError as V:
    print(V);
