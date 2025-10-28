class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self,rootvalue):
        self.root=Node(rootvalue)
    def insert(self,value):
        self._insert_recursive(self.root,value)
    def _insert_recursive(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left=Node(value)
            else:
                self._insert_recursive(current_node.left,value)
        else:
            if current_node.right is None:
                current_node.right=Node(value)
            else:
                self._insert_recursive(current_node.right,value)
    def search(self,value):
        return self._search_recursive(self.root,value)
    def _search_recursive(self,current_node,value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left,value)
        else:
            return self._search_recursive(current_node.right,value)