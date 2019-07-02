##this is an implementation of Shell Sort in Python3
class shell:
    def __init__(self,items):
        self.items=items;
        length=len(self.items);
        gap=length//2;
        strt=0;
        pas=0;
        while gap>0:
            for i in range(strt+gap,length):
                for j in range(i,gap-1,-gap):
                    if self.items[j-gap]>self.items[j]:
                        self.items[j],self.items[j-gap]=self.items[j-gap],self.items[j];
            gap//=2;
            pas+=1;
            print(pas);
    def sorted(self):
        return self.items;