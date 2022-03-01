class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        node = self.root
        def ins(node,data):
            if node == None:
                return
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    ins(node.left,data)
            if data > node.data:
                if node.right == None:
                    node.right = Node(data)
                else:
                    ins(node.right,data)
        ins(node,data)
        

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)
    
    def find(self, data):
        if self.root:
            a = self.ins(self.root,data)
        if self.root:
            if a:
                return True
            else:
                return False
        return None
    
    def ins(self,node,data):
            if node == None:
                return
            print(data,node.data)
            if node.data == data:
                return True
            if data < node.data:
                if node.left == None:
                    return False
                else:
                    self.ins(node.left,data)
            if data > node.data:
                if node.right == None:
                    return False
                else:
                    self.ins(node.right,data)
    

    '''
    def find(self, data):
        if self.root:
            is_found = self._find(self.root,data)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self,cur_node,data):
        if data > cur_node.data and cur_node.right:
            return self._find(cur_node.right,data)
        elif data < cur_node.data and cur_node.left:
            return self._find(cur_node.left, data)
        if data == cur_node.data:
            return True
    '''
    def is_bst_satisfied(self):
        a = self.checktree(self.root)
        if a == None:
            return True
        return False

    def checktree(self,node):
        if node == None:
            return 
        if node.left:
            if node.left.data > node.data:
                return False
            else:
                self.checktree(node.left)
        if node.right:
            if node.right.data < node.data:
                return False
            else:
                self.checktree(node.right)

    

bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
bst.insert(15)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.find(1))
bst.inorder_print_tree()
print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())
#print(tree.is_bst_satisfied())