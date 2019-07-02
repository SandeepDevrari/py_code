##this is an implementation of Merge Sort in python 3
class merge:
    def __init__(self,items):
        self.sorted_arry=self.divide_conquer(items);
    def divide_conquer(self,items):
        length=len(items);
        if length==1:		##base case
            return items;
## Dividing List
        mid=length//2;
        item1=self.divide_conquer(items[:mid]);
        item2=self.divide_conquer(items[mid:]);
##Merging list in sorted order
        i,j=0,0;
        item3=[];
        while i<len(item1) or j<len(item2):
            if i>=len(item1) or j>=len(item2):
                if i>=len(item1):
                    item3.append(item2[j]);
                    j+=1;
                else:
                    item3.append(item1[i]);
                    i+=1;
            elif item1[i]>item2[j]:
                item3.append(item2[j]);
                j+=1;
            else:
                item3.append(item1[i]);
                i+=1;
        else:
            return item3;
    def sorted(self):
        return self.sorted_arry;