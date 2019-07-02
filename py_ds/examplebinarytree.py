##this is an implementation of Tree in python3
## Node class
class node:
    def __init__(self,item):
        self.data=item;
        self.L=None;
        self.R=None;
##Tree class
class binary_tree:
    def __init__(self,items):
        if items==None:
            print("No Tree!!");
        else:
            i=0;
            self.root=node(items[i]);
            i+=1;
            if len(items)>1:
                self.built_tree(items[i:])
    def built_tree(self,items):
        if items!=None:
            i=0;
            temp=node(items[i]);
            i+=1;
            self.linker=self.root;
            self.link_tree(temp);
            if len(items)>1:
                self.built_tree(items[i:])
    def link_tree(self,link):
        if self.linker.L!=link and self.linker.R!=link:
            ##p,s=str(link.data),str(self.linker.data);
            if link.data<=self.linker.data:
                if self.linker.L==None:
                    self.linker.L=link;
                else:
                    self.linker=self.linker.L;
                    self.link_tree(link);
            else:
                if self.linker.R==None:
                    self.linker.R=link;
                else:
                    self.linker=self.linker.R;
                    self.link_tree(link);
##tree traversing
##inorder
    def inorder(self):
        link=self.root;
        def in_inorder(link):
            if link!=None:
                in_inorder(link.L);
                print(str(link.data)+" ",end='');
                in_inorder(link.R);
        in_inorder(link);
        print(" ");
##preorder
    def preorder(self):
        link=self.root;
        def pre_preorder(link):
            if link!=None:
                print(str(link.data)+" ",end='');
                pre_preorder(link.L);
                pre_preorder(link.R);
        pre_preorder(link);
        print(" ");
##postorder
    def postorder(self):
        link=self.root;
        def post_postorder(link):
            if link!=None:
                post_postorder(link.L);
                post_postorder(link.R);
                print(str(link.data)+" ",end='');
        post_postorder(link);
        print(" ");
##Insert && Delete Operations
##Insert
    def insert(self,item):
         link=node(item);
         self.linker=self.root;
         self.link_tree(link);
##Delete
    def delete(self,item):
        next,pre=self.in_search(item);
        if next!=None:
            if next.L==None and next.R==None:
                if next==pre.L:
                    pre.L=None;
                else:
                    pre.R=None;
            elif next.L==None or next.R==None:
                if next.L!=None:
                    if next==pre.L:
                        pre.L=next.L;
                    else:
                        pre.R=next.L;
                else:
                    if next==pre.R:
                        pre.L=next.R;
                    else:
                        pre.R=next.R;
            else:
                successor,pre=next.R,next;
                while successor.L!=None:
                    pre,successor=successor,successor.L;
                else:
                    next.data=successor.data;
                    if pre==next:
                        pre.R=None;
                    else:
                        pre.L=None;
    def in_search(self,item):
        next,pre=self.root,self.root;
        while next!=None:
            if next.data==item:
                return next,pre;
            elif item<next.data:
                pre,next=next,next.L;
            else:
                pre,next=next,next.R;
        else:
            return next,pre;
##Search
    def search(self,item):
        next,pre=self.in_search(item);
        if next==None:
            return False;
        else:
            return True;