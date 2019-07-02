##this is an implementation of node in python3
##this class is required for implementation of unordered lists in python3
class node:
    def __init__(self,item):
        self.data=item;
        self.next=None;
    def get_data(self):
        return self.data;
    def get_next(self):
        return self.next;
    def set_data(self,item):
        self.data=item;
    def set_next(self,address):
        self.next=address;