#implementing stack using linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top is None:
            return "list is empty"
        else:
            deletednode=self.top
            self.top=self.top.next
            return deletednode.data
    def display(self):
        elements=[]
        currentnode=self.top
        while currentnode:
            elements.append(currentnode.data)
            currentnode=currentnode.next
        return elements