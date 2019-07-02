##this is an implementation of Quick Sort in python3
class quick:
    def __init__(self,items):
        self.item=items;
        lindex,rindex=0,len(self.item)-1;
        self.divide_conquer(lindex,rindex);
    def divide_conquer(self,lindex,rindex):
        if lindex!=rindex and lindex<rindex:
            start,end=lindex,rindex;
            pivot,pivot_point,pindex=self.item[lindex],'L',lindex;
            while lindex!=rindex:
                if pivot_point=='L':
                    if pivot>self.item[rindex]:
                        self.item[lindex],self.item[rindex]=self.item[rindex],self.item[lindex];
                        pivot_point,pindex='R',rindex;
                    else:
                        rindex-=1;
                else:
                    if pivot<self.item[lindex]:
                        self.item[lindex],self.item[rindex]=self.item[rindex],self.item[lindex];
                        pivot_point,pindex='L',lindex;
                    else:
                        lindex+=1;
            else:
                self.divide_conquer(start,pindex-1);
                self.divide_conquer(pindex+1,end);
    def sorted(self):
        return self.item;
