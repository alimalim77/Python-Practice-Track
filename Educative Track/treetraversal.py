
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
            one = one.dequeue()
            if start.left:
                one.enqueue(start.left)
            if start.right:
                one.enqueue(start.right)
        return travstr
        
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


b = tree.print_tree("level")
print(b)