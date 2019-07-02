##this is an implementation of Deque by using list in python3
class deque:
    def __init__(self):
        self.items=[];
    def add_front(self,item):
        self.items.append(item);
    def add_rear(self,item):
        self.items.insert(0,item);
    def remove_front(self):
        return self.items.pop();
    def remove_rear(self):
        return self.items.pop(0);
    def peek_rear(self):
        return self.items[0];
    def peek_front(self):
        return self.items[len(self.items)];
    def size(self):
        return len(self.items);
    def show_deque(self):
        return self.items[::];
    def is_empty(self):
        return self.items==[];
