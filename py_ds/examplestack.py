#this is an example of stack in python3 with the help of list
class stack:
    def __init__(self):
        self.items=[];
    def push(self,top):
        self.items.append(top);
    def pop(self):
        return self.items.pop();
    def peek(self):
        return self.items[len(self.items)-1];
    def size(self):
        return len(self.items);
    def show_stack(self):
        return self.items;
    def is_empty(self):
        return self.items==[];
