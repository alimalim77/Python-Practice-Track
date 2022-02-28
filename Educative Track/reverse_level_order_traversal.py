"""
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
    
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
    
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("levelorder"))
"""

from inspect import trace
from logging import root

class Stack:
    def __init__(self):
        self.s = []
    
    def push(self,val):
        self.s.append(val)
    
    def pop(self):
        self.s.pop()

    def isempty(self):
        if len(self.s) == 0:
            return True

    def peak(self):
        return self.s[-1].val

    def totalele(self):
        return self.s[::-1]



class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def isEmpty(self):
        return True if self.queue == [] else False

    def peak(self):
        if len(self.queue) > 0:
            return self.queue[-1].val
    
    
    


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def reverselevelorder(self,node):
        if not node:
            return
        print(node.val)
        q = Queue()
        s = Stack()
        q.enqueue(node)
        while q:
            if q.peak() == None:
                print(s.totalele())
                return
            node1 = q.dequeue()
            #print(node1.val)
            s.push(node1.val)
            print(s.totalele())
            
            if node1.left:
                q.enqueue(node1.left)
            if node1.right:
                q.enqueue(node1.right)
            
            
            
        


        

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(42)
tree.root.right.right = Node(57)
tree.root.right.right.left = Node(65)
tree.reverselevelorder(tree.root)
    
