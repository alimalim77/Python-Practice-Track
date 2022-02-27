class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        if self.head == None:
            self.head = Node(val)
            return
        
        cur = self.head
        while cur.next != None:
            cur = cur.next
        suc = Node(val) 
        cur.next = suc
        suc.prev = cur 
        
    def prepend(self,val):
        if self.head == None:
            self.head = Node(val)
            return
        cur = self.head
        pre = Node(val)
        cur.prev = pre
        pre.next = cur
        self.head = pre
    
    def printlist(self):
        if not self.head:
            return
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next 

dd = DoublyLinkedList()
dd.append(5)
dd.append(7)
dd.append(15)
dd.append(74)
dd.prepend(2)
dd.append(9)
dd.printlist()

    

        