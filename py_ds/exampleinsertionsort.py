##this is an inplementation of Insertion sort in python3
class insertion:
    def __init__(self,items):
        self.items=items;
        for i in range(1,len(self.items)):
            for j in range(i,0,-1):
                if self.items[j-1]>self.items[j]:
                    self.items[j],self.items[j-1]=self.items[j-1],self.items[j];
    def sorted(self):
        return self.items;