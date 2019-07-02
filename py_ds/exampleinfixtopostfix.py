#this is the program for converting infix expression to postfix expression
#this program uses stack
import examplestack
class in_to_post:
    def __init__(self,data):
        stk=examplestack.stack();
        self.data_list=[];
        self.op_dict={'(':0,')':0,'^':3,'*':2,'/':2,'%':2,'+':1,'-':1};
        for i in data:
            if i not in self.op_dict:
                self.data_list.append(i);
            else:
                if stk.is_empty():
                    if i==')':
                        print("Error");
                        exit(0);
                    stk.push(i);
                else:
                    if i==')':
                        temp=stk.pop();
                        while temp!='(':
                            self.data_list.append(temp);
                            temp=stk.pop();
                    else:
                        if self.op_dict[i]>self.op_dict[stk.peek()] or i=='(':
                            stk.push(i);
                        elif self.op_dict[i]<self.op_dict[stk.peek()]:
                            self.data_list.append(stk.pop());
                            while not stk.is_empty():
                                if self.op_dict[i]>self.op_dict[stk.peek()]:
                                    stk.push(i);
                                    break;
                                elif self.op_dict[i]==self.op_dict[stk.pop()]:
                                    self.data_list.append(stk.pop());
                                    stk.push(i);
                                    break;
                                else:
                                    self.data_list.append(stk.pop());
                            else:
                                stk.push(i);
                        else:
                            self.data_list.append(stk.pop());
                            stk.push(i);
        while not stk.is_empty():
            self.data_list.append(stk.pop());
    def return_bck(self):
        return self.data_list;
