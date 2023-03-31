#      2
#  3      5
# 4     4 7
# class Node:
# 	def __init__(self, val):	
# 		self.val = val
# 		self.left = None
# 		self.right = None

        
# def count(node,ctr):
	
# 	if (node == None):
# 		return 0
# 	return (count(node.left) + count(node.right) + 1)

# def checkRec(root, n):
# 	#global res
# 	# Base case
# 	if (root == None): return 0
# 	c = checkRec(root.left, n) + 1 + checkRec(root.right, n)

	# if (c == n - c):
	# 	res = True

	# return c

class Node:
    
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def totalNodes(self,root):
        if root == None:
            return 0 
        return self.totalNodes(root.left) + 1 + self.totalNodes(root.right)
    def nodechecker(self,root,n,c):
        if root == None:
            return 0 
        c = 0
        c += self.nodechecker(root.left,n,c) + 1 + self.nodechecker(root.right,n,c)

        if c == n//2:
            self.flag = True
        return c


root = Node(8)
root.left = Node(6)
root.right = Node(13)
root.left.left = Node(2)
root.right.left = Node(9)
root.right.right = Node(15)
root.flag = False


n = root.totalNodes(root)
print(n)
if n% 2 != 0:
    print("NO")
    exit()
root.nodechecker(root,n,0)
if root.flag:
    print("YES")
else:
    print("NO")

