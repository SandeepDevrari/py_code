#this is an implementation of hash in python3
class hash:
    def __init__(self,size):
        self.size=size;
        self.slots=[None]*self.size;
        self.data=[None]*self.size;
    def hash_fun(self,item):
        return item%self.size;    
    def put(self,item,data):
        self.hash_value=self.hash_fun(item);
        if self.slots[self.hash_value]==None:
            self.slots[self.hash_value]=item;
            self.data[self.hash_value]=data;
        else:
            if self.slots[self.hash_value]==item:
                self.data[self.hash_value]=data;
            else:
                next_slot=self.rehash(self.hash_value);
                while self.slots[next_slot] != None and self.slots[next_slot] !=item:
                    next_slot = self.rehash(next_slot)
                if self.slots[next_slot]==None:
                    self.slots[next_slot]=item;
                    self.data[next_slot]=data;
                else:
                    self.data[next_slot]=data;
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size;

    def get(self, key):
        start_slot = self.hash_fun(key);
        dat = None;
        stop = False;
        found = False;
        position = start_slot;
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True;
                dat = self.data[position];
            else:
                position=self.rehash(position)
                if position == start_slot:
                    stop = True
        return dat;

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
