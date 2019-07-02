##this is an implementation of binary search in python3
class binary:
    def search(self,items,item):
        if len(items)==0:
            return False;
        ###self.start=items[0];
        ##self.end=items[len(items)];
        self.mid=len(items)//2;
        if items[self.mid]==item:
            return True;
        else:
            if item<items[self.mid]:
                return self.search(items[:self.mid],item);
            else:
                return self.search(items[self.mid+1:],item);
