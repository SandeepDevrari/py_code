##this is the module for menu
class menu:
    def __init__(self,*var):
        self.c=0;
        print("\t\t\tMENU-->");
        for i in var:
            self.c+=1;
            print("\t\t%d: %s"%(self.c,i));
        self.c=input("\tEnter Your Choice:");
    def menu_return(self):
        return self.c;        

