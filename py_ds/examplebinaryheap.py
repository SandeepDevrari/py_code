##this is an implementation of Binary Heap in python 3
class binaryheap:
    def __init__(self,items):
        self.items=items;
        self.value=False;
        self.items.insert(0,0);
        ##self.items.append(None);
        self.size=len(self.items)-1;
        self.min_heap(1,'c');
##Binary Heap Operations
    def min_heap(self,pos,check):
        if check=='c':
            if (2*pos)<=(self.size):
                self.heap_child(pos);
                self.min_heap(pos+1,'c');
        else:
            if pos>0 and self.value==False:
                self.heap_papa(pos);
                self.min_heap(pos//2,'p');
    def heap_child(self,pos):
        if (2*pos)<=(self.size):
            if self.items[pos]>self.items[2*pos]:
                self.items[pos],self.items[2*pos]=self.items[2*pos],self.items[pos];
            if ((2*pos)+1)<=(self.size):
                if self.items[pos]>self.items[(2*pos)+1]:
                    self.items[pos],self.items[(2*pos)+1]=self.items[(2*pos)+1],self.items[pos];
    def heap_papa(self,pos):
        if pos>0:
            if self.items[pos]<self.items[(pos//2)]:
                self.items[pos],self.items[pos//2]=self.items[pos//2],self.items[pos];
            else:
                self.value=True;
    def heap_display(self):
        for i in range(1,self.size+1):
            print(str(self.items[i])+" ",end='');
        print(" ");
    def heap_insert(self,item):
        self.items.append(item);
        self.size=len(self.items)-1;
        self.value=False;
        self.min_heap(self.size,'p');
    def heap_delete(self):
        item=self.items[self.size];
        self.items[1]=item;
        self.items.pop();
        self.size=len(self.items)-1;
        self.min_heap(1,'c');