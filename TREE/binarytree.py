class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class binarytree:
    def __init__(self,rootvalue):
        self.root = node(rootvalue)
    def print_inorder(self):
        self._inorder_recursive(self.root)
        print()
    def _inorder_recursive(self,node):
        if node:
            self._inorder_recursive(node.left)
            print(node.value, end='')
            self._inorder_recursive(node.right)
    def print_preorder(self):
        self._preorder_recursive(self.root)
        print()
    def _preorder_recursive(self,node):
        if node:
            print(node.value, end='')
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)
    def print_postorder(self):
        self._postorder_recursive(self.root)
        print()
    def _postorder_recursive(self,node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.value, end='')
    def insert_left(self,current_node,value):
        current_node.left = node(value)
    def insert_right(self,current_node,value):
        current_node.right = node(value)

tree1=binarytree(1)
tree1.insert_left(tree1.root,2)
tree1.insert_right(tree1.root,3)
tree1.insert_left(tree1.root.left,4)
tree1.insert_right(tree1.root.left,5)
tree1.insert_left(tree1.root.right,6)
tree1.insert_right(tree1.root.right,7)
tree1.print_inorder()
tree1.print_preorder()
tree1.print_postorder()    
        


   


            
        