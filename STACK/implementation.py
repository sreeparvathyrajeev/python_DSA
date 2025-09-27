class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def display(self):
        return self.items           
s=stack()
s.push(1)
s.push(2)
s.push(3)
print(s.display())
print(s.pop())
print(s.display())
print(s.peek())
print(s.size())
print(s.isEmpty())  