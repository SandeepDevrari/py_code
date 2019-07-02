##this is an implementation of linked list in python3
##to do this required examplenode file
import examplenode
class linkedlist:
    def __init__(self):
        self.head=None;
    def add_node(self,item):
        temp=examplenode.node(item);
        temp.set_next(self.head);
        self.head=temp;
    def is_empty(self):
        return self.head==None;
    def insert_node(self,position,item):
        pre,temp=self.index(position);
        if temp==False:
            return;
        temp1=examplenode(item);
        temp1.set_next(pre.get_next());
        pre.set_next(temp1);
    def append_node(self,item):
        count=self.size_list();
        if count==False:
            return;
        pre,temp=self.index(count);
        if temp==False:
            return;
        temp1=examplenode.node(item);
        temp.set_next(temp1);
    def size_list(self):
        temp=self.head;
        if temp==None:
            return False;
        count=1;
        while temp!=None:
            temp=temp.get_next();
            count+=1;
        else:
            return count;
    def index(self,position):
        count=1;
        temp=self.head;
        if temp==None:
            return False,False;
        pre=None;
        while count!=position:
            pre=temp;
            temp=temp.get_next();
            count+=1;
        else:
            return pre,temp;
    def search_node(self,item):
        temp=self.head;
        count=1;
        while temp.get_data()!=item:
            if temp==None:
                return False;
            temp=temp.get_next();
            count+=1;
        else:
            return count;
    def del_head(self):
        temp=self.head;
        if temp==None:
            return;
        self.head=temp.get_next();
    def del_tail(self):
        count=self.size_list();
        if count==False:
            return;
        pre,temp=self.index(count);
        if temp==False:
            return;
        pre.set_next==None;
    def delete_node(self,position):
        pre,temp=self.index(position);
        if temp==False:
            return False;
        pre.set_next(temp.get_next());
