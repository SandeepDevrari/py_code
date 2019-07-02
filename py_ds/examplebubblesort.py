##this is an inplementation of Bubble sort in python3
class bubble:
    def __init__(self,items):
        self.items=items;
        for i in range(len(self.items)-1,0,-1):
            for j in range(i):
                if self.items[j]>self.items[j+1]:
                    self.items[j],self.items[j+1]=self.items[j+1],self.items[j];
    def sorted(self):
        return self.items;