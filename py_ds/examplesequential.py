##this is an implementation of sequential search in python3
class sequential :
    def search(self,items,item):
        self.pos=0;
        while self.pos < len(items):
            if items[self.pos]==item: 
                return True,self.pos;
            self.pos+=1;
        else:
            return False,None;

    def ordered_search(self,items,item):
        self.pos=0;
        while self.pos < len(items):
            if items[self.pos]==item: 
                return True,self.pos;
            if items[self.pos]>item: 
                return False,None;
            self.pos+=1;
        else:
            return False,None;
