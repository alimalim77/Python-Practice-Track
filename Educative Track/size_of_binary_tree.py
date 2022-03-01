
from logging import root


class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self,val):

        self.q.append(val)
    
    def dequeue(self):
        if len(self.q) == 0:
            print('Queue is empty')
        self.q.pop(0)
    
    def peek(self):
        if len(self.q) >0:
            return self.q[0]

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()

    def print(self):
        return self.stack


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
        elif traversal_type == 'level':
            one = Queue()
            return self.level_traversal(tree.root,one)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
            self.ctr += 1
            #maxctr = max(maxctr,ctr)
        print("Max Depth is", ctr)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def level_traversal(self,start,one):
        if start == None:
            return
        travstr = ''
        one.enqueue(start)
        while len(one.q) != 0:
            travstr = travstr + str(one.peek().value)
            print(one.peek())
            start = one.dequeue()
            if start.left:
                one.enqueue(start.left)
            if start.right:
                one.enqueue(start.right)
        return travstr
    
    def maxheight(self,node):
        if node.left == None and node.right == None:
            return 1
        if node == None:
            return 0
        left = self.maxheight(node.left)
        right = self.maxheight(node.right)

        return 1 + max(left,right)
    s = Stack()
    def sizetree(self,node,ctr =0):
        
        if node == None:
            return 
        
        self.sizetree(node.left,ctr)
        self.s.push(node.value)
        print(node.value)
        self.sizetree(node.right,ctr)
        return len(self.s.print())
        
        

        

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
ans = tree.sizetree(tree.root)
print("size is", ans)