##this is an inplementation of Selection sort in python3
class selection:
    def __init__(self,items):
        self.items=items;
        for i in range(len(self.items)-1,0,-1):
            strt=0;
            for j in range(1,i+1):
                if self.items[j]>self.items[strt]:
                    strt=j;
            self.items[j],self.items[strt]=self.items[strt],self.items[j];
    def sorted(self):
        return self.items;