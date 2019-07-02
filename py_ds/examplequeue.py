##this is an implementation of queue in python3 with the help of list
class queue:
    def __init__(self):
        self.items=[];
    def enqueue(self,item):
        self.items.insert(0,item);
    def dequeue(self):
        return self.items.pop();
    def is_empty(self):
        return self.items==[];
    def size(self):
        return len(self.items);
    def peek(self):
        return self.items[len(self.items)-1];
    def show_queue(self):
        return self.items[::-1];
