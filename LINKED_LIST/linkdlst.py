class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_end(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    
    def insert_at_position(self,value,position):
        new_node=node(value)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        for i in range(position-1):
            temp=temp.next
        save=temp.next
        temp.next=new_node
        new_node.next=save

    