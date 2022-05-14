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
for i in range(4000000):
    tree.add_value(randint(-100000,100000))
    

tree.print_tree()    
            
        
