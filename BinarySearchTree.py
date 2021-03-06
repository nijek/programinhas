from random import seed
from random import randint
import sys
sys.setrecursionlimit(17500)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = left
    
    def add_value(self, value):
        node = Node(value)
        self.add_node(Node(value))
        
    
    def add_node(self, node):
        
        if node.value > self.value:
            if self.right == None:
                self.right = node
            else:
                self.right.add_node(node)
        elif node.value < self.value:
            if self.left == None:
                self.left = node
            else:
     
                self.left.add_node(node)

    def traversal(self):
        if self.left:
            self.left.traversal()
        print(self.value)
        if self.right:
            self.right.traversal()
    
    def print_node(self):
        print(self.value)
        if self.left != None:
            self.left.print_node()
        else:
            print("LEFT NULL")
        if self.right != None:
            self.right.print_node()
        else:
            print("RIGHT NULL")

class BinaryTree(Node): 
    def __init__(self, value):
        super().__init__(value)
        self.value = value
        self.left = None
        self.right = None
    def root(self):
        return self.value
    def search_value(self, value):
        pass
    def min(self):
        val = self.value
        left = self.left
        while left != None:
            val = left.value
            left = left.left
        return val 
    def max(self):
        val = self.value
        right = self.right
        while right != None:
            val = right.value
            right = right.right
        return val  
    
    def add_value(self, value):
        node = Node(value)
        self.add_node(Node(value))
    
    

    
    def print_tree(self):
        print (self.value)
        if self.left != None:
            self.left.print_node()
        else:
            print("LEFT NULL")
        if self.right != None:
            self.right.print_node()
        else:
            print("RIGHT NULL")
    

seed()  
tree = BinaryTree(randint(-10000,10000))       
for i in range(4):
    tree.add_value(randint(-100000,100000))
    

#print(tree.min(), tree.max())   
tree.traversal()
print("\n\n")
print(tree.min(), tree.max())
            
        
