##this is the program for implementeing the linked list in with the help examplelinkedlist file
import examplemenu
import examplelinkedlist
class link:
    def __init__(self):
        menu_obj=examplemenu.menu("create list");
        choice=menu_obj.menu_return();
        if choice!='1':
            print("wrong choice!!");
            exit(0);
        list=examplelinkedlist.linkedlist();
        item=input("\t\t\tlist is created!!\n\t\tEnter data: ");
        list.add_node(item);
        menu_obj1=examplemenu.menu("Add head);

